import matplotlib.pyplot as plt
import pandas as pd

# db is in upper directory
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import get_engine

def plot_coin_chart(coin: str) -> None:
    """Estrae da db i prezzi di coin e mostra il grafico."""
    engine = get_engine()
    with engine.connect() as conn:
        df = pd.read_sql(f"SELECT date, price FROM prices WHERE symbol = '{coin}' ORDER BY date", conn)
    
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['price'], marker='o')
    plt.title(f'Price Chart for {coin}')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    coin = os.getenv("COIN", "bitcoin")
    plot_coin_chart(coin)