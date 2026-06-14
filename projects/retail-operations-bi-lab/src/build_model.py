from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SAMPLE_DIR = ROOT / "data" / "sample"
POWERBI_DIR = ROOT / "data" / "powerbi"
OUTPUT_DIR = ROOT / "output"


def read_sources() -> dict[str, pd.DataFrame]:
    return {
        "stores": pd.read_csv(SAMPLE_DIR / "stores.csv", parse_dates=["open_date"]),
        "products": pd.read_csv(SAMPLE_DIR / "products.csv"),
        "customers": pd.read_csv(SAMPLE_DIR / "customers.csv", parse_dates=["signup_date"]),
        "sales": pd.read_csv(SAMPLE_DIR / "sales.csv", parse_dates=["sale_date"]),
        "inventory": pd.read_csv(SAMPLE_DIR / "inventory.csv", parse_dates=["snapshot_date"]),
        "deliveries": pd.read_csv(SAMPLE_DIR / "deliveries.csv", parse_dates=["promised_date", "delivered_date"]),
    }


def validate_sources(sources: dict[str, pd.DataFrame]) -> list[str]:
    issues: list[str] = []
    for name, df in sources.items():
        if df.empty:
            issues.append(f"{name}: source is empty")
        if df.isna().sum().sum() > 0:
            issues.append(f"{name}: contains null values")

    sales = sources["sales"]
    products = sources["products"]
    stores = sources["stores"]
    customers = sources["customers"]

    if not sales["product_id"].isin(products["product_id"]).all():
        issues.append("sales: invalid product_id found")
    if not sales["store_id"].isin(stores["store_id"]).all():
        issues.append("sales: invalid store_id found")
    if not sales["customer_id"].isin(customers["customer_id"]).all():
        issues.append("sales: invalid customer_id found")
    if (sales["quantity"] <= 0).any():
        issues.append("sales: quantity must be positive")
    if (sales["discount_rate"] < 0).any() or (sales["discount_rate"] >= 1).any():
        issues.append("sales: discount_rate must be between 0 and 1")
    return issues


def build_date_dimension(sales: pd.DataFrame, inventory: pd.DataFrame) -> pd.DataFrame:
    dates = pd.concat(
        [
            sales["sale_date"].rename("date"),
            inventory["snapshot_date"].rename("date"),
        ],
        ignore_index=True,
    ).drop_duplicates()
    dim_date = pd.DataFrame({"date": pd.to_datetime(dates).sort_values().reset_index(drop=True)})
    dim_date["date_key"] = dim_date["date"].dt.strftime("%Y%m%d").astype(int)
    dim_date["year"] = dim_date["date"].dt.year
    dim_date["month_number"] = dim_date["date"].dt.month
    dim_date["month_name"] = dim_date["date"].dt.strftime("%b")
    dim_date["year_month"] = dim_date["date"].dt.strftime("%Y-%m")
    dim_date["quarter"] = "Q" + dim_date["date"].dt.quarter.astype(str)
    return dim_date[["date_key", "date", "year", "quarter", "month_number", "month_name", "year_month"]]


def build_fact_sales(sales: pd.DataFrame, dim_date: pd.DataFrame) -> pd.DataFrame:
    fact = sales.merge(dim_date[["date", "date_key"]], left_on="sale_date", right_on="date", how="left")
    fact["gross_sales"] = fact["quantity"] * fact["unit_price"]
    fact["discount_amount"] = fact["gross_sales"] * fact["discount_rate"]
    fact["net_sales"] = fact["gross_sales"] - fact["discount_amount"]
    fact["cost_amount"] = fact["quantity"] * fact["unit_cost"]
    fact["gross_margin"] = fact["net_sales"] - fact["cost_amount"]
    return fact[
        [
            "sale_id",
            "date_key",
            "store_id",
            "product_id",
            "customer_id",
            "channel",
            "quantity",
            "gross_sales",
            "discount_amount",
            "net_sales",
            "cost_amount",
            "gross_margin",
        ]
    ]


def build_fact_inventory(inventory: pd.DataFrame, dim_date: pd.DataFrame) -> pd.DataFrame:
    fact = inventory.merge(dim_date[["date", "date_key"]], left_on="snapshot_date", right_on="date", how="left")
    fact["stockout_risk"] = (fact["on_hand_units"] <= fact["reorder_point"]).astype(int)
    return fact[["date_key", "store_id", "product_id", "on_hand_units", "reorder_point", "stockout_risk"]]


def build_fact_delivery(deliveries: pd.DataFrame, sales: pd.DataFrame, dim_date: pd.DataFrame) -> pd.DataFrame:
    fact = deliveries.merge(sales[["sale_id", "sale_date", "store_id", "customer_id"]], on="sale_id", how="left")
    fact = fact.merge(dim_date[["date", "date_key"]], left_on="sale_date", right_on="date", how="left")
    fact["delivery_days"] = (fact["delivered_date"] - fact["sale_date"]).dt.days
    fact["promised_days"] = (fact["promised_date"] - fact["sale_date"]).dt.days
    fact["is_late"] = (fact["delivered_date"] > fact["promised_date"]).astype(int)
    return fact[["sale_id", "date_key", "store_id", "customer_id", "delivery_method", "delivery_days", "promised_days", "is_late"]]


def write_outputs(tables: dict[str, pd.DataFrame]) -> None:
    POWERBI_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, df in tables.items():
        df.to_csv(POWERBI_DIR / f"{name}.csv", index=False)

    sales = tables["fact_sales"]
    inventory = tables["fact_inventory"]
    delivery = tables["fact_delivery"]
    summary = {
        "net_sales": round(float(sales["net_sales"].sum()), 2),
        "gross_margin": round(float(sales["gross_margin"].sum()), 2),
        "margin_rate": round(float(sales["gross_margin"].sum() / sales["net_sales"].sum()), 4),
        "orders": int(sales["sale_id"].nunique()),
        "stockout_risk_rows": int(inventory["stockout_risk"].sum()),
        "late_delivery_rate": round(float(delivery["is_late"].mean()), 4),
    }
    pd.DataFrame([summary]).to_csv(OUTPUT_DIR / "kpi_summary.csv", index=False)

    report = [
        "# Retail Operations Summary",
        "",
        f"- Net sales: {summary['net_sales']:,.2f}",
        f"- Gross margin: {summary['gross_margin']:,.2f}",
        f"- Margin rate: {summary['margin_rate']:.2%}",
        f"- Orders: {summary['orders']:,}",
        f"- Inventory rows at stockout risk: {summary['stockout_risk_rows']:,}",
        f"- Late delivery rate: {summary['late_delivery_rate']:.2%}",
    ]
    (OUTPUT_DIR / "business_summary.md").write_text("\n".join(report), encoding="utf-8")


def main() -> None:
    sources = read_sources()
    issues = validate_sources(sources)
    if issues:
        raise SystemExit("\n".join(issues))

    dim_date = build_date_dimension(sources["sales"], sources["inventory"])
    tables = {
        "dim_date": dim_date,
        "dim_store": sources["stores"],
        "dim_product": sources["products"],
        "dim_customer": sources["customers"],
        "fact_sales": build_fact_sales(sources["sales"], dim_date),
        "fact_inventory": build_fact_inventory(sources["inventory"], dim_date),
        "fact_delivery": build_fact_delivery(sources["deliveries"], sources["sales"], dim_date),
    }
    write_outputs(tables)
    print(f"Power BI model tables written to {POWERBI_DIR}")
    print(f"Business summary written to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
