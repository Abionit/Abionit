# Power BI Report Blueprint

## Model

Import the CSV files from `data/powerbi/`.

Relationships:

- `fact_sales[date_key]` -> `dim_date[date_key]`
- `fact_sales[store_id]` -> `dim_store[store_id]`
- `fact_sales[product_id]` -> `dim_product[product_id]`
- `fact_sales[customer_id]` -> `dim_customer[customer_id]`
- `fact_inventory[date_key]` -> `dim_date[date_key]`
- `fact_inventory[store_id]` -> `dim_store[store_id]`
- `fact_inventory[product_id]` -> `dim_product[product_id]`
- `fact_delivery[date_key]` -> `dim_date[date_key]`
- `fact_delivery[store_id]` -> `dim_store[store_id]`
- `fact_delivery[customer_id]` -> `dim_customer[customer_id]`

Use single-direction filtering from dimensions to facts.

## Page 1: Executive Overview

Cards:

- Net Sales
- Gross Margin
- Margin Rate
- Orders
- Late Delivery Rate
- Stockout Risk Count

Visuals:

- Net Sales by Month
- Net Sales and Margin Rate by Category
- Net Sales by Region
- Customer Segment Contribution

Decision focus:

- identify where revenue is growing,
- detect margin pressure,
- compare regions and customer segments.

## Page 2: Store And Inventory Operations

Visuals:

- Stockout Risk Count by Store
- Average On Hand Units by Category
- Net Sales vs Stockout Risk by Store
- Store ranking table with Net Sales, Margin Rate, Stockout Risk Count

Decision focus:

- prioritize replenishment,
- identify stores losing sales due to low availability,
- compare operational performance by location.

## Page 3: Fulfillment And Customer Impact

Visuals:

- Late Delivery Rate by Delivery Method
- Average Delivery Days by Region
- Orders and Late Delivery Rate by Month
- Customer Segment table with Sales Per Customer

Decision focus:

- review delivery methods with higher delay rates,
- connect fulfillment issues with customer segments,
- prioritize process improvements.

## Recommended Slicers

- Year Month
- Region
- Store
- Category
- Channel
- Customer Segment
