"""
One-time script: clean the raw Tickertape export into data/holdings_real.csv
Input:  data/holdings_raw.csv  (paste your Tickertape export here, unmodified)
Output: data/holdings_real.csv (ticker, quantity_held, avg_buy_price)
"""
import pandas as pd

RAW_PATH = "data/holdings_raw.csv"
OUTPUT_PATH = "data/holdings_real.csv"


def load_raw_holdings(path: str) -> pd.DataFrame:
    # TODO: read the CSV. Hint: pd.read_csv has a `skiprows` param —
    # count how many lines come before the real header row
    # ("Security,No. of Smallcases,Quantity,...")
    df = pd.read_csv(RAW_PATH, skiprows=3)
    return df

def clean_holdings(df: pd.DataFrame) -> pd.DataFrame:
    # TODO 1: drop rows after (and including) the "Smallcases" section
    #   Hint: find the row index where df["Security"] == "Smallcases", slice before it
    smallcases_idx = df.iloc[1:38]
    # TODO 2: select just Security, Quantity, "Average Cost ₹"
    smallcases_idx=smallcases_idx[["Security", "Quantity", "Average Cost â¹"]]    
    # TODO 3: rename columns -> ticker, quantity_held, avg_buy_price
    smallcases_idx=smallcases_idx.rename(columns={'Security':'ticker', 'Quantity':'quantity_held', 'Average Cost â¹':'avg_buy_price'})
    # TODO 4: append ".NS" to every ticker
    smallcases_idx['ticker'] = smallcases_idx['ticker'].astype(str) + '.NS'
    return smallcases_idx


if __name__ == "__main__":
    raw = load_raw_holdings(RAW_PATH)
    cleaned = clean_holdings(raw)
    cleaned.to_csv(OUTPUT_PATH, index=False)
    print(f"Wrote {len(cleaned)} holdings to {OUTPUT_PATH}")
