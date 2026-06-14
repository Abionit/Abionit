from __future__ import annotations

import random
from datetime import date, timedelta
from pathlib import Path

import pandas as pd


random.seed(21)

ROOT = Path(__file__).resolve().parents[1]
SAMPLE_DIR = ROOT / "data" / "sample"


def date_range(start: date, days: int) -> list[date]:
    return [start + timedelta(days=offset) for offset in range(days)]


def generate_stores() -> pd.DataFrame:
    cities = [
        ("Bogota", "Andean"),
        ("Medellin", "Andean"),
        ("Cali", "Pacific"),
        ("Cartagena", "Caribbean"),
        ("Barranquilla", "Caribbean"),
        ("Bucaramanga", "Andean"),
        ("Pereira", "Coffee Region"),
        ("Santa Marta", "Caribbean"),
    ]
    rows = []
    for idx, (city, region) in enumerate(cities, start=1):
        rows.append(
            {
                "store_id": idx,
                "store_name": f"{city} Store",
                "city": city,
                "region": region,
                "open_date": f"202{random.randint(0, 3)}-{random.randint(1, 12):02d}-01",
            }
        )
    return pd.DataFrame(rows)


def generate_products() -> pd.DataFrame:
    categories = {
        "Personal Care": ["Shampoo", "Soap", "Toothpaste", "Skin Cream"],
        "Health": ["Vitamin C", "Pain Relief", "Thermometer", "Bandages"],
        "Baby": ["Diapers", "Baby Wipes", "Baby Lotion"],
        "Home": ["Detergent", "Disinfectant", "Paper Towels"],
        "Beauty": ["Makeup Kit", "Hair Treatment", "Sunscreen"],
    }
    rows = []
    product_id = 1
    for category, products in categories.items():
        for product in products:
            unit_cost = round(random.uniform(3.5, 42.0), 2)
            list_price = round(unit_cost * random.uniform(1.25, 1.95), 2)
            rows.append(
                {
                    "product_id": product_id,
                    "product_name": product,
                    "category": category,
                    "unit_cost": unit_cost,
                    "list_price": list_price,
                }
            )
            product_id += 1
    return pd.DataFrame(rows)


def generate_customers(count: int = 850) -> pd.DataFrame:
    segments = ["Retail", "Loyalty", "Wholesale", "Online"]
    rows = []
    for customer_id in range(1, count + 1):
        rows.append(
            {
                "customer_id": customer_id,
                "customer_segment": random.choices(segments, weights=[45, 30, 10, 15])[0],
                "signup_date": str(date(2023, 1, 1) + timedelta(days=random.randint(0, 720))),
                "city": random.choice(["Bogota", "Medellin", "Cali", "Cartagena", "Barranquilla", "Pereira"]),
            }
        )
    return pd.DataFrame(rows)


def generate_sales(stores: pd.DataFrame, products: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    rows = []
    sale_id = 1
    calendar = date_range(date(2025, 1, 1), 180)
    for current_date in calendar:
        for _ in range(random.randint(40, 95)):
            product = products.sample(1, random_state=random.randint(1, 999_999)).iloc[0]
            quantity = random.choices([1, 2, 3, 4, 5, 8, 10], weights=[30, 25, 18, 12, 8, 5, 2])[0]
            discount_rate = random.choice([0, 0, 0.03, 0.05, 0.08, 0.10, 0.15])
            channel = random.choices(["Store", "Online", "Phone"], weights=[65, 30, 5])[0]
            rows.append(
                {
                    "sale_id": sale_id,
                    "sale_date": str(current_date),
                    "store_id": int(stores.sample(1, random_state=random.randint(1, 999_999)).iloc[0]["store_id"]),
                    "product_id": int(product["product_id"]),
                    "customer_id": int(customers.sample(1, random_state=random.randint(1, 999_999)).iloc[0]["customer_id"]),
                    "quantity": quantity,
                    "unit_price": float(product["list_price"]),
                    "unit_cost": float(product["unit_cost"]),
                    "discount_rate": discount_rate,
                    "channel": channel,
                }
            )
            sale_id += 1
    return pd.DataFrame(rows)


def generate_inventory(stores: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    rows = []
    snapshot_dates = [date(2025, 1, 31), date(2025, 2, 28), date(2025, 3, 31), date(2025, 4, 30), date(2025, 5, 31), date(2025, 6, 30)]
    for snapshot_date in snapshot_dates:
        for _, store in stores.iterrows():
            for _, product in products.iterrows():
                on_hand = random.randint(0, 220)
                reorder_point = random.randint(18, 55)
                rows.append(
                    {
                        "snapshot_date": str(snapshot_date),
                        "store_id": int(store["store_id"]),
                        "product_id": int(product["product_id"]),
                        "on_hand_units": on_hand,
                        "reorder_point": reorder_point,
                    }
                )
    return pd.DataFrame(rows)


def generate_deliveries(sales: pd.DataFrame) -> pd.DataFrame:
    online_sales = sales[sales["channel"].isin(["Online", "Phone"])].copy()
    rows = []
    for _, sale in online_sales.iterrows():
        sale_date = date.fromisoformat(sale["sale_date"])
        promised_days = random.choice([1, 2, 3, 4])
        actual_days = max(0, int(random.gauss(promised_days + 0.4, 1.1)))
        rows.append(
            {
                "sale_id": int(sale["sale_id"]),
                "delivery_method": random.choice(["Courier", "Motorbike", "Pickup Partner"]),
                "promised_date": str(sale_date + timedelta(days=promised_days)),
                "delivered_date": str(sale_date + timedelta(days=actual_days)),
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    SAMPLE_DIR.mkdir(parents=True, exist_ok=True)
    stores = generate_stores()
    products = generate_products()
    customers = generate_customers()
    sales = generate_sales(stores, products, customers)
    inventory = generate_inventory(stores, products)
    deliveries = generate_deliveries(sales)

    for name, df in {
        "stores": stores,
        "products": products,
        "customers": customers,
        "sales": sales,
        "inventory": inventory,
        "deliveries": deliveries,
    }.items():
        df.to_csv(SAMPLE_DIR / f"{name}.csv", index=False)

    print(f"Sample data written to {SAMPLE_DIR}")


if __name__ == "__main__":
    main()
