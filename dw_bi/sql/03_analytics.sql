-- 1) Vendite per categoria (fatturato)
SELECT
    p.category,
    ROUND(SUM(f.extended_amount), 2) AS revenue
FROM dw.fact_orders f
JOIN dw.dim_products p ON p.product_id = f.product_id
GROUP BY p.category
ORDER BY revenue DESC;

-- 2) Top 5 clienti per fatturato
SELECT
    c.customer_code,
    c.first_name || ' ' || c.last_name AS customer_name,
    ROUND(SUM(f.extended_amount), 2) AS revenue
FROM dw.fact_orders f
JOIN dw.dim_customers c ON c.customer_id = f.customer_id
GROUP BY c.customer_code, customer_name
ORDER BY revenue DESC
LIMIT 5;

-- 3) Trend mensile delle vendite
SELECT
    d.year,
    d.month,
    ROUND(SUM(f.extended_amount), 2) AS revenue
FROM dw.fact_orders f
JOIN dw.dim_dates d ON d.date_id = f.date_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;
