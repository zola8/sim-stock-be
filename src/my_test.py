import yfinance as yf

if __name__ == '__main__':
    ticker = yf.Ticker("INVALID")
    print(ticker.info)

    if not ticker.info or 'regularMarketPrice' not in ticker.info:
        print("Ticker not found")
