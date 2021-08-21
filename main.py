# https://pypi.org/project/yfinance/
import typer
import numpy as np
import pandas as pd
import yfinance as yf


app = typer.Typer()


@app.command()
def price(stock: str):
    """Give the current stock price"""
    stock_data = yf.Ticker(stock.upper())

    typer.echo(f"Stock Price: {stock_data.info['regularMarketPrice']}")


@app.command()
def risk(stock: str):
    """Give the risk associated with stock, mutual fund or etf"""
    stock_data = yf.Ticker(stock.upper()).info
    # stock_data_dict = {
    #     "Stock": stock.upper(),
    #     "Industry": stock_data["industry"],
    #     "Beta": stock_data["beta"],
    #     "Market Cap": stock_data["marketCap"],
    # }
    # df = pd.DataFrame(stock_data_dict, index=[1, 2, 3, 4])
    typer.echo(
        f"Stock: {stock.upper()}\nIndustry: {stock_data['industry']}\nBeta {stock_data['beta']: .2f}\nMarkent Cap: {stock_data['marketCap']: .2f}\nOpen: {stock_data['open']: .2f}"
    )


if __name__ == "__main__":
    app()
