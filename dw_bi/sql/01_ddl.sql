-- Create a simple e‑commerce star schema in Postgres
CREATE SCHEMA IF NOT EXISTS dw;

-- Dimension tables
CREATE TABLE IF NOT EXISTS dw.dim_customers (
    customer_id     INT PRIMARY KEY,
    customer_code   TEXT NOT NULL,
    first_name      TEXT,
    last_name       TEXT,
    email           TEXT,
    country         TEXT,
    city            TEXT,
    signup_date     DATE
);

CREATE TABLE IF NOT EXISTS dw.dim_products (
    product_id   INT PRIMARY KEY,
    sku          TEXT NOT NULL,
    product_name TEXT NOT NULL,
    category     TEXT,
    brand        TEXT,
    unit_price   NUMERIC(10,2)
);

CREATE TABLE IF NOT EXISTS dw.dim_dates (
    date_id    INT PRIMARY KEY, -- yyyymmdd
    date       DATE NOT NULL,
    year       INT,
    month      INT,
    day        INT,
    week       INT,
    is_weekend INT
);

-- Fact table
CREATE TABLE IF NOT EXISTS dw.fact_orders (
    order_id        INT PRIMARY KEY,
    date_id         INT NOT NULL REFERENCES dw.dim_dates(date_id),
    customer_id     INT NOT NULL REFERENCES dw.dim_customers(customer_id),
    product_id      INT NOT NULL REFERENCES dw.dim_products(product_id),
    quantity        INT NOT NULL,
    unit_price      NUMERIC(10,2) NOT NULL,
    discount        NUMERIC(5,2) NOT NULL DEFAULT 0,
    extended_amount NUMERIC(10,2) NOT NULL,
    currency        TEXT NOT NULL,
    order_ts        TIMESTAMP DEFAULT NOW()
);
