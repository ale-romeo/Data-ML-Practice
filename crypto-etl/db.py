import os
import sqlalchemy

def get_engine() -> "sqlalchemy.Engine":
    """Crea l'engine da os.environ['DB_URL'] (default sqlite:///data/crypto.db)."""
    db_url = os.getenv("DB_URL", "sqlite:///data/crypto.db")
    return sqlalchemy.create_engine(db_url)

def init_db() -> None:
    """Esegue lo script SQL di init schema."""
    engine = get_engine()
    with engine.connect() as conn:
        with open("scripts/init_db.sql", "r", encoding="utf-8") as f:
            sql = f.read()
        conn.execute(sqlalchemy.text(sql))
        conn.commit()
        conn.close()

def upsert_prices(rows: list[dict]) -> int:
    """
    Inserisce righe in prices.
    rows: [{symbol:str, date:datetime.date|str 'YYYY-MM-DD', price:float}, ...]
    - SQLite: INSERT OR IGNORE
    - Postgres: ON CONFLICT (symbol,date) DO NOTHING
    Ritorna il numero di righe tentate (o inserite).
    """
    engine = get_engine()
    with engine.connect() as conn:
        if engine.dialect.name == "sqlite":
            sql = """
            INSERT OR IGNORE INTO prices (symbol, date, price)
            VALUES (:symbol, :date, :price)
            """
        elif engine.dialect.name == "postgresql":
            sql = """
            INSERT INTO prices (symbol, date, price)
            VALUES (:symbol, :date, :price)
            ON CONFLICT (symbol, date) DO NOTHING
            """
        else:
            raise ValueError(f"Unsupported database dialect: {engine.dialect.name}")
        conn.execute(sqlalchemy.text(sql), rows)
        conn.commit()
        conn.close()
        return len(rows)