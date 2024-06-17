# app.py
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output

from load_data import load_stock_data
from plots import plot_line_chart, plot_candlestick_chart, plot_correlation_heatmap, plot_bar_chart


tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']
stock_data = load_stock_data(tickers)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Stock Market Analysis Dashboard"), className="mb-4")
    ]),
    dbc.Row([
        dbc.Col(dcc.Dropdown(
            id='ticker-dropdown',
            options=[{'label': ticker, 'value': ticker} for ticker in tickers],
            value='AAPL',
            className="mb-4"
        ), width=4)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='line-chart'), width=6),
        dbc.Col(dcc.Graph(id='candlestick-chart'), width=6),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='bar-chart'), width=6),
        dbc.Col(dcc.Graph(id='correlation-heatmap', figure=plot_correlation_heatmap(stock_data)), width=6),
    ])
], fluid=True)

@app.callback(
    [Output('line-chart', 'figure'),
     Output('candlestick-chart', 'figure'),
     Output('bar-chart', 'figure')],
    [Input('ticker-dropdown', 'value')]
)
def update_charts(ticker):
    line_chart = plot_line_chart(stock_data[ticker], ticker)
    candlestick_chart = plot_candlestick_chart(stock_data[ticker], ticker)
    bar_chart = plot_bar_chart(stock_data[ticker], ticker)
    return line_chart, candlestick_chart, bar_chart

if __name__ == '__main__':
    app.run_server(debug=True)
