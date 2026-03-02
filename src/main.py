import logging

import uvicorn
import yfinance as yf

from src.config.setup_fastapi import setup_fastapi
from src.config.setup_logging import setup_logging
from src.finance_tickers import load_nasdaq_screener_data, fetch_ticker_data

logger = logging.getLogger(__name__)
setup_logging()
app = setup_fastapi()


@app.get("/ticker-list")
def get_ticker_list():
    return load_nasdaq_screener_data()


@app.get("/fetch/ticker/{ticker_id}")
def fetch_ticker(ticker_id: str):
    return fetch_ticker_data(ticker_id)


@app.get("/")
def home():
    return {
        "yf": yf.__version__,
        "nasdaq_screener": "2026-03-01"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, forwarded_allow_ips='*')
