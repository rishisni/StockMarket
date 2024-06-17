
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def plot_line_chart(stock_data, ticker):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_data.index, 
                             y=stock_data['Close'], 
                             mode='lines', 
                             name=ticker,
                             line=dict(color='royalblue', width=2)))
    fig.update_layout(title=f'{ticker} Stock Prices Over Time',
                      xaxis_title='Date',
                      yaxis_title='Price (USD)',
                      template='plotly_dark')
    return fig

def plot_candlestick_chart(stock_data, ticker):
    fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                         open=stock_data['Open'],
                                         high=stock_data['High'],
                                         low=stock_data['Low'],
                                         close=stock_data['Close'],
                                         increasing_line_color='green', 
                                         decreasing_line_color='red')])
    fig.update_layout(title=f'{ticker} Candlestick Chart',
                      xaxis_title='Date',
                      yaxis_title='Price (USD)',
                      template='plotly_white')
    return fig

def plot_correlation_heatmap(stock_data):
    close_prices = pd.DataFrame({ticker: data['Close'] for ticker, data in stock_data.items()})
    correlation_matrix = close_prices.corr()
    
    fig = px.imshow(correlation_matrix,
                    text_auto=True,
                    labels=dict(x="Stock", y="Stock", color="Correlation"),
                    x=correlation_matrix.columns,
                    y=correlation_matrix.columns,
                    color_continuous_scale='Viridis')
    fig.update_layout(title='Correlation Heatmap of Stock Closing Prices',
                      template='plotly_dark')
    return fig

def plot_bar_chart(stock_data, ticker):
    fig = go.Figure(data=[go.Bar(x=stock_data.index, y=stock_data['Volume'], name='Volume', marker_color='black')])
    fig.update_layout(title=f'{ticker} Trading Volume Over Time',
                      xaxis_title='Date',
                      yaxis_title='Volume',
                      template='xgridoff')
    return fig
