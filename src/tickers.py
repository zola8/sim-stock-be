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
    history: dict
    info: dict
    isin: str
    income_stmt: dict | None
    recommendations: dict | None
    revenue_estimate: dict | None


def load_ticker_list(filename: str) -> dict:
    df = pd.read_csv(filename)
    logger.debug("Initial data: {} rows loaded".format(df.shape[0]))
    return df.to_dict()


def convert_timestamps(history_dict):
    result = {}
    for (metric, symbol), data in history_dict.items():
        result[(metric, symbol)] = {
            timestamp.strftime('%Y-%m-%d'): value
            for timestamp, value in data.items()
        }
    return result


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

    df = yf.download(ticker_symbol.strip().upper(), period='max')
    history = convert_timestamps(df.to_dict())

    return TickerResponse(
        history=history,
        info=ticker.info,
        isin=ticker.isin.upper(),
        income_stmt=ticker.ttm_income_stmt.to_json(),
        recommendations=ticker.recommendations.to_json(),
        revenue_estimate=ticker.revenue_estimate.to_json(),
    )
