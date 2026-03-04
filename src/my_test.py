import os
from pathlib import Path
from pprint import pprint

import yfinance as yf

from src.fileutils import get_file_path

if __name__ == '__main__':
    # pprint(fetch_ticker_data('epam'))
    # df = yf.download('epam', period='3d')
    # history = convert_timestamps(df.to_dict())
    # pprint(history)

    # ticker = yf.Ticker('epam')
    # pprint(ticker.get_major_holders())

    # load_ticker_list()

    filename = 'data/test.csv'
    aa = get_file_path(filename)
    print(aa)
