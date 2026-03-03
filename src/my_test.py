from pprint import pprint

import yfinance as yf

from src.finance_tickers import fetch_ticker_data, convert_timestamps

if __name__ == '__main__':
    # pprint(fetch_ticker_data('epam'))
    df = yf.download('epam', period='3d')
    history = convert_timestamps(df.to_dict())
    pprint(history)
