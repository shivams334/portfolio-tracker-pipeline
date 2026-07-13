"""
One-time script: enrich cleaned holdings with company metadata via yfinance.
Input:  data/holdings_real.csv  (ticker, quantity_held, avg_buy_price)
Output: data/holdings_enriched.csv
        (ticker, company_name, sector, industry, market_cap_category,
         quantity_held, avg_buy_price)
"""
import pandas as pd
import yfinance as yf

INPUT_PATH = "data/holdings_real.csv"
OUTPUT_PATH = "data/holdings_enriched.csv"

# Market cap category thresholds (INR). Tune these however you like.
LARGE_CAP_MIN = 20000_00_00_000    # 20,000 Cr
MID_CAP_MIN = 5000_00_00_000       # 5,000 Cr


def load_holdings(path: str) -> pd.DataFrame:
    # TODO: read the CSV at `path` into a DataFrame and return it.
    pass


def fetch_metadata(ticker: str) -> dict:
    # TODO: create a yf.Ticker object for `ticker`, pull its `.info` dict,
    # and return a plain dict with keys: ticker, company_name, sector,
    # industry, market_cap (raw number).
    #   - company_name  <- info.get("longName")
    #   - sector        <- info.get("sector")
    #   - industry      <- info.get("industry")
    #   - market_cap    <- info.get("marketCap")
    # Some tickers may be missing fields (or the API call could fail) —
    # decide how you want to handle that (e.g. fall back to None) so one
    # bad ticker doesn't crash the whole loop.
    pass


def categorize_market_cap(market_cap) -> str:
    # TODO: given a raw market_cap number, return "large_cap", "mid_cap",
    # or "small_cap" using LARGE_CAP_MIN / MID_CAP_MIN above.
    # Think about what should happen if market_cap is None/missing.
    pass


def build_metadata_frame(tickers: list[str]) -> pd.DataFrame:
    # TODO: loop over `tickers`, call fetch_metadata() for each, and collect
    # the results into a single DataFrame (one row per ticker).
    # Hint: build a list of dicts as you go, then pd.DataFrame(that_list).
    pass


def enrich_holdings(holdings: pd.DataFrame, metadata: pd.DataFrame) -> pd.DataFrame:
    # TODO: merge `holdings` (ticker, quantity_held, avg_buy_price) with
    # `metadata` (ticker, company_name, sector, industry, market_cap) on
    # "ticker", apply categorize_market_cap() to produce
    # "market_cap_category", and return a DataFrame with exactly these
    # columns in this order:
    # ticker, company_name, sector, industry, market_cap_category,
    # quantity_held, avg_buy_price
    pass


if __name__ == "__main__":
    holdings = load_holdings(INPUT_PATH)
    metadata = build_metadata_frame(holdings["ticker"].tolist())
    enriched = enrich_holdings(holdings, metadata)
    enriched.to_csv(OUTPUT_PATH, index=False)
    print(f"Wrote {len(enriched)} enriched holdings to {OUTPUT_PATH}")
