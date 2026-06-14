-- Revenue and margin by store
SELECT
    s.region,
    s.city,
    s.store_name,
    SUM(f.net_sales) AS net_sales,
    SUM(f.gross_margin) AS gross_margin,
    SUM(f.gross_margin) * 1.0 / NULLIF(SUM(f.net_sales), 0) AS margin_rate
FROM fact_sales f
JOIN dim_store s ON f.store_id = s.store_id
GROUP BY s.region, s.city, s.store_name
ORDER BY net_sales DESC;

-- Category performance
SELECT
    p.category,
    SUM(f.quantity) AS units_sold,
    SUM(f.net_sales) AS net_sales,
    SUM(f.gross_margin) AS gross_margin,
    SUM(f.gross_margin) * 1.0 / NULLIF(SUM(f.net_sales), 0) AS margin_rate
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY net_sales DESC;

-- Stockout risk by store and category
SELECT
    s.store_name,
    p.category,
    SUM(i.stockout_risk) AS stockout_risk_rows,
    AVG(i.on_hand_units) AS avg_on_hand_units
FROM fact_inventory i
JOIN dim_store s ON i.store_id = s.store_id
JOIN dim_product p ON i.product_id = p.product_id
GROUP BY s.store_name, p.category
ORDER BY stockout_risk_rows DESC, avg_on_hand_units ASC;

-- Delivery performance
SELECT
    delivery_method,
    COUNT(*) AS deliveries,
    AVG(delivery_days) AS avg_delivery_days,
    SUM(is_late) AS late_deliveries,
    SUM(is_late) * 1.0 / COUNT(*) AS late_delivery_rate
FROM fact_delivery
GROUP BY delivery_method
ORDER BY late_delivery_rate DESC;

-- Customer segment contribution
SELECT
    c.customer_segment,
    COUNT(DISTINCT f.customer_id) AS customers,
    SUM(f.net_sales) AS net_sales,
    SUM(f.net_sales) * 1.0 / COUNT(DISTINCT f.customer_id) AS sales_per_customer
FROM fact_sales f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.customer_segment
ORDER BY net_sales DESC;
