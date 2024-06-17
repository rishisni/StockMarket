
import pandas as pd

def load_stock_data(tickers):
    stock_data = {}
    for ticker in tickers:
        stock_data[ticker] = pd.read_csv(f'{ticker}.csv', index_col='Date', parse_dates=True)
    return stock_data

if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']
    stock_data = load_stock_data(tickers)
    for ticker, data in stock_data.items():
        print(f'{ticker} data:')
        print(data.head())
