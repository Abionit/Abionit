# Business Case

## Context

A retail operation sells through physical stores, online orders, and phone orders. The company tracks sales, customers, inventory, products, and deliveries in separate operational files.

The commercial team can see total sales, but it is harder to understand whether performance issues come from margin, inventory availability, late deliveries, channel mix, or customer segment behavior.

## Problem

The business needs a reporting layer that answers operational questions without rebuilding spreadsheets every week.

Key issues:

- revenue is separated from inventory and delivery performance,
- product margin is not visible in the same model as sales,
- stores with stockout risk are not easy to prioritize,
- late deliveries are not connected to customer and store context,
- analysts need reusable tables instead of manual calculations.

## Modeling Logic

The model uses a star schema because the reporting questions are analytical. Dimensions describe the business context. Fact tables store measurable events.

Dimensions:

- date,
- store,
- product,
- customer.

Facts:

- sales,
- inventory snapshots,
- deliveries.

This structure keeps Power BI relationships simple and makes SQL analysis easier to review.

## Data Quality Controls

The build process checks:

- empty source files,
- null values,
- invalid product, store, or customer references,
- non-positive sales quantities,
- discount rates outside the expected range.

The pipeline stops if a critical rule fails.

## Business Recommendations

The final model supports three types of recommendations:

1. Margin review  
   Categories with strong revenue but weak margin should be reviewed for discounting, cost, or pricing issues.

2. Inventory prioritization  
   Stores and categories with repeated stockout risk should be prioritized for replenishment and demand planning.

3. Fulfillment improvement  
   Delivery methods with higher late delivery rates should be reviewed before they affect customer experience.

## Why This Project Matters

The value is not only the dashboard. The value is the process behind it: data is connected, validated, modeled, and prepared so business teams can trust the metrics.
