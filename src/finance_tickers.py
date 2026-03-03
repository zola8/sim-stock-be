import logging
from dataclasses import dataclass
from typing import Optional

import pandas as pd
import yfinance as yf
from fastapi import HTTPException, status

logger = logging.getLogger(__name__)


@dataclass
class TickerResponse:
    """Class for keeping info and historical data together for a stock."""
    history: str | None
    info: dict | None


def load_ticker_list() -> str:
    df = pd.read_csv('data/test.csv')
    logger.debug("Initial data: {} rows loaded".format(df.shape[0]))
    return df.to_json()


def fetch_ticker_data(ticker_symbol: Optional[str] = None) -> TickerResponse:
    if not ticker_symbol or not isinstance(ticker_symbol, str) or not ticker_symbol.strip():
        logger.warning(f"Error: Invalid ticker value: {ticker_symbol}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid ticker value provided."
        )

    ticker = yf.Ticker(ticker_symbol)
    if not ticker.info or 'regularMarketPrice' not in ticker.info:
        logger.warning(f"Error: Ticker not found: {ticker_symbol}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Ticker not found: {ticker_symbol}"
        )

    df = yf.download(ticker_symbol.strip().upper(), period='3d')

    return TickerResponse(history=df.to_json(), info=ticker.info)
