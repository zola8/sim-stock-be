from pprint import pprint

from src.config.setup_logging import setup_logging
from src.finance_tickers import fetch_ticker_data

if __name__ == '__main__':
    setup_logging()
    epam = fetch_ticker_data('epam')
    pprint(epam)
