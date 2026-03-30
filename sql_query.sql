SELECT
    p.category,
    DATE_TRUNC('month', o.order_date) AS month,
    SUM(o.revenue) AS total_revenue
FROM orders o
LEFT JOIN products p
    ON o.product_id = p.product_id
GROUP BY
    p.category,
    DATE_TRUNC('month', o.order_date)
ORDER BY
    p.category,
    month;
