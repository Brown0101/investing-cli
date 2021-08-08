# https://pypi.org/project/yfinance/
import typer
import yfinance as yf
import json

app = typer.Typer()


@app.command()
def price(stock: str):
    """Give the current stock price"""
    stock_data = yf.Ticker(stock.upper())

    typer.echo(f"Stock Price: {stock_data.info['regularMarketPrice']}")


@app.command()
def risk(stock: str):
    """Give the risk associated with stock, mutual fund or etf"""

    # TODO: Need to implement to find sharpe ratio, alpha, beta, standard diviation, and R-Squared.
    typer.echo(f"Stock Risk: {stock}")


if __name__ == "__main__":
    app()
