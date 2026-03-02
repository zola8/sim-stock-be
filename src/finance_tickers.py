import logging
from dataclasses import dataclass
from typing import Optional

import pandas as pd
import yfinance as yf

logger = logging.getLogger(__name__)


@dataclass
class TickerResponse:
    """Class for keeping info and historical data together for a stock."""
    history: str | None
    info: dict | None
    error: str | None = None


def load_ticker_list() -> str:
    df = pd.read_csv('data/test.csv')
    logger.debug("Initial data: {} rows loaded".format(df.shape[0]))
    return df.to_json()


def fetch_ticker_data(ticker: Optional[str] = None) -> TickerResponse:
    if not ticker or not isinstance(ticker, str) or not ticker.strip():
        logger.warning(f"Error: Invalid ticker value: {ticker}")
        return TickerResponse(history=None, info=None, error="Invalid ticker value")

    df = yf.download(ticker.strip().upper(), period='3d')
    info = yf.Ticker(ticker=ticker.strip().upper()).info

    return TickerResponse(history=df.to_json(), info=info, error=None)
