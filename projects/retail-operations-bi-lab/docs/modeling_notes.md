# Modeling Notes

## Why A Star Schema

The project uses a star schema because Power BI reporting works best when dimensions filter facts through clear one-to-many relationships.

This avoids a common reporting issue: large flat tables that mix customer, product, inventory, and delivery fields until the model becomes hard to validate.

## Facts

`fact_sales` stores transactional sales measures:

- quantity,
- gross sales,
- discount amount,
- net sales,
- cost amount,
- gross margin.

`fact_inventory` stores periodic inventory snapshots:

- on-hand units,
- reorder point,
- stockout risk flag.

`fact_delivery` stores fulfillment measures:

- delivery days,
- promised days,
- late delivery flag.

## Dimensions

`dim_date` supports time intelligence and month-level reporting.

`dim_store` supports region, city, and location analysis.

`dim_product` supports category and product analysis.

`dim_customer` supports segment-level reporting.

## Power BI Design Decision

The repository includes CSV model tables and DAX measures instead of a `.pbix` file. That makes the project easier to review in GitHub and avoids hiding the logic inside a binary file.

The dashboard can still be rebuilt in Power BI using the model blueprint.
