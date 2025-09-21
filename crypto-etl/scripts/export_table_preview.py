import pandas as pd
# db is in upper directory
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import get_engine

def export_table_preview() -> None:
    """Esporta un'anteprima della tabella prices."""
    engine = get_engine()
    with engine.connect() as conn:
        df = pd.read_sql_table("prices", conn)
        print(df.head())

if __name__ == "__main__":
    export_table_preview()