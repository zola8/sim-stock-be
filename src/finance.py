import logging

import pandas as pd

logger = logging.getLogger(__name__)


def load_nasdaq_screener_data() -> str:
    df = pd.read_csv('data/nasdaq_screener_20260301.csv')
    logger.debug("Initial data: {} rows loaded".format(df.shape[0]))
    return df.to_json()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    pd.set_option('display.max_columns', 100)
    load_nasdaq_screener_data()
