import logging
from dataclasses import dataclass
from typing import Optional

import pandas as pd
import yfinance as yf

logger = logging.getLogger(__name__)


@dataclass
class TickerResponse:
    data: str
    error: str


def load_ticker_list() -> str:
    df = pd.read_csv('data/test.csv')
    logger.debug("Initial data: {} rows loaded".format(df.shape[0]))
    return df.to_json()


def fetch_ticker_data(ticker: Optional[str] = None) -> TickerResponse:
    if not ticker or not isinstance(ticker, str) or not ticker.strip():
        logger.warning(f"Error: Invalid ticker value: {ticker}")
        return TickerResponse(data="", error="Invalid ticker value")

    df = yf.download(ticker.strip().upper(), period='3d')
    return TickerResponse(data=df.to_json(), error="")
