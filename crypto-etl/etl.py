import requests
import pandas as pd
import os
from db import init_db, upsert_prices

def fetch_coin_prices(coin: str, vs_currency: str, days: str) -> "pd.DataFrame":
    """
    Chiama l'endpoint storico (CoinGecko market_chart) e ritorna
    DataFrame con colonne: ts_ms (int), price (float).
    """
    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"
    params = {"vs_currency": vs_currency, "days": days}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()
    df = pd.DataFrame(data["prices"], columns=["ts_ms", "price"])
    return df

def normalize_prices(df_raw: "pd.DataFrame", coin: str) -> "pd.DataFrame":
    """
    Converte ts_ms → date UTC (YYYY-MM-DD), rimuove null, tiene l'ultimo prezzo per ogni data,
    aggiunge column 'symbol'. Ritorna colonne: ['symbol','date','price'].
    """
    df = df_raw.copy()
    df["date"] = pd.to_datetime(df["ts_ms"], unit="ms", utc=True).dt.date
    df = df.drop(columns=["ts_ms"])
    df = df.dropna(subset=["price"])
    df["symbol"] = coin
    df = df.sort_values(by=["date", "price"]).drop_duplicates(subset=["date"], keep="last")
    df = df[["symbol", "date", "price"]]
    return df

def get_highest_price_in_period(df: "pd.DataFrame", start_date: str, end_date: str) -> float:
    """
    Ritorna il prezzo più alto in df tra start_date e end_date (inclusi).
    start_date, end_date: str 'YYYY-MM-DD'
    """
    mask = (df["date"] >= pd.to_datetime(start_date).date()) & (df["date"] <= pd.to_datetime(end_date).date())
    highest_price = df.loc[mask, "price"].max()
    return highest_price

def main() -> None:
    """
    - legge env (COINS, VS_CURRENCY, DAYS)
    - init_db()
    - loop sulle coin
    - stampa righe fetchate e risultato upsert
    """
    coins = os.getenv("COINS", "bitcoin,ethereum").split(",")
    vs_currency = os.getenv("VS_CURRENCY", "usd")
    days = os.getenv("DAYS", "30")
    init_db()

    for coin in coins:
        print(f"Fetching prices for {coin}...")
        df_raw = fetch_coin_prices(coin, vs_currency, days)
        df = normalize_prices(df_raw, coin)
        rows = df.to_dict(orient="records")
        print(f"Fetched {len(rows)} rows for {coin}.")
        inserted = upsert_prices(rows)
        print(f"Inserted {inserted} rows for {coin}.")
        
        highest_price = get_highest_price_in_period(df, "2025-08-17", "2025-09-17")
        print(f"Highest price for {coin} in 2025: {highest_price}")
    print("Done.")

if __name__ == "__main__":
    main()