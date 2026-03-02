import logging

import uvicorn
import yfinance as yf
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.finance import load_nasdaq_screener_data

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/get-initial-data")
def get_initial_data():
    return {
        "nasdaq_screener": load_nasdaq_screener_data()
    }


@app.get("/")
def home():
    return {
        "yf": yf.__version__,
        "nasdaq_screener": "2026-03-01"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, forwarded_allow_ips='*')
