from __future__ import annotations

import unittest
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
POWERBI_DIR = ROOT / "data" / "powerbi"


class RetailModelTests(unittest.TestCase):
    def test_powerbi_tables_exist(self) -> None:
        expected = {
            "dim_date.csv",
            "dim_store.csv",
            "dim_product.csv",
            "dim_customer.csv",
            "fact_sales.csv",
            "fact_inventory.csv",
            "fact_delivery.csv",
        }
        actual = {path.name for path in POWERBI_DIR.glob("*.csv")}
        self.assertTrue(expected.issubset(actual))

    def test_fact_sales_values_are_valid(self) -> None:
        sales = pd.read_csv(POWERBI_DIR / "fact_sales.csv")
        self.assertFalse(sales.empty)
        self.assertTrue((sales["quantity"] > 0).all())
        self.assertTrue((sales["net_sales"] >= 0).all())
        self.assertTrue((sales["gross_sales"] >= sales["discount_amount"]).all())

    def test_relationship_keys_are_valid(self) -> None:
        sales = pd.read_csv(POWERBI_DIR / "fact_sales.csv")
        stores = pd.read_csv(POWERBI_DIR / "dim_store.csv")
        products = pd.read_csv(POWERBI_DIR / "dim_product.csv")
        customers = pd.read_csv(POWERBI_DIR / "dim_customer.csv")
        self.assertTrue(sales["store_id"].isin(stores["store_id"]).all())
        self.assertTrue(sales["product_id"].isin(products["product_id"]).all())
        self.assertTrue(sales["customer_id"].isin(customers["customer_id"]).all())

    def test_delivery_late_flag_is_binary(self) -> None:
        delivery = pd.read_csv(POWERBI_DIR / "fact_delivery.csv")
        self.assertTrue(set(delivery["is_late"].unique()).issubset({0, 1}))


if __name__ == "__main__":
    unittest.main()
