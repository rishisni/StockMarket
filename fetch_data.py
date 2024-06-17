
import yfinance as yf
import pandas as pd

def fetch_stock_data(tickers, start_date, end_date):
    stock_data = {}
    for ticker in tickers:
        stock_data[ticker] = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']
    start_date = '2020-01-01'
    end_date = '2023-01-01'
    stock_data = fetch_stock_data(tickers, start_date, end_date)
    
    for ticker in tickers:
        stock_data[ticker].to_csv(f'{ticker}.csv')
