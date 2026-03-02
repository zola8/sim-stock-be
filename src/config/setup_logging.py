import logging


def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    )
    logging.getLogger("yfinance").setLevel(logging.INFO)
    logging.getLogger("peewee").setLevel(logging.INFO)
