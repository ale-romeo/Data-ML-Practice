-- Load CSVs into Postgres (inside container paths!)
\copy dw.dim_customers  FROM '/repo/data/dim_customers.csv'  CSV HEADER;
\copy dw.dim_products   FROM '/repo/data/dim_products.csv'   CSV HEADER;
\copy dw.dim_dates      FROM '/repo/data/dim_dates.csv'      CSV HEADER;
-- STAGING per fact_orders (il CSV ha order_date che non è in fact)
CREATE TABLE IF NOT EXISTS dw.stg_fact_orders (
  order_id        INT,
  date_id         INT,
  order_date      DATE,
  customer_id     INT,
  product_id      INT,
  quantity        INT,
  unit_price      NUMERIC(10,2),
  discount        NUMERIC(5,2),
  extended_amount NUMERIC(10,2),
  currency        TEXT
);

\copy dw.stg_fact_orders FROM '/repo/data/fact_orders.csv' CSV HEADER;

INSERT INTO dw.fact_orders (order_id, date_id, customer_id, product_id, quantity, unit_price, discount, extended_amount, currency)
SELECT order_id, date_id, customer_id, product_id, quantity, unit_price, discount, extended_amount, currency
FROM dw.stg_fact_orders
ON CONFLICT (order_id) DO NOTHING;

DROP TABLE dw.stg_fact_orders;

