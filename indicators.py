import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st 
from data import get_stock_data
def calculate_indicators(data):
    """
    Calculate all technical indicators.
    """
    # Daily Return
    data["Daily Return"] = data["Close"].pct_change() * 100
    # Moving Averages
    data["MA20"] = data["Close"].rolling(20).mean()
    data["MA50"] = data["Close"].rolling(50).mean()
    data["MA200"] = data["Close"].rolling(200).mean()
    # Exponential Moving Average
    data["EMA20"] = data["Close"].ewm(span=20, adjust=False).mean()
    data["EMA50"] = data["Close"].ewm(span=50, adjust=False).mean()
    # RSI
    delta = data["Close"].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()
    rs = avg_gain / avg_loss
    data["RSI"] = 100 - (100 / (1 + rs))
    # MACD
    ema12 = data["Close"].ewm(span=12, adjust=False).mean()
    ema26 = data["Close"].ewm(span=26, adjust=False).mean()
    data["MACD"] = ema12 - ema26
    data["Signal"] = data["MACD"].ewm(span=9, adjust=False).mean()
    # Bollinger Bands
    rolling_std = data["Close"].rolling(20).std()
    data["Upper Band"] = data["MA20"] + (2 * rolling_std)
    data["Lower Band"] = data["MA20"] - (2 * rolling_std)
    # ATR (Average True Range)

    high_low = data["High"] - data["Low"]
    high_close = abs(data["High"] - data["Close"].shift())
    low_close = abs(data["Low"] - data["Close"].shift())
    true_range = pd.concat(
        [high_low, high_close, low_close],
        axis=1
    ).max(axis=1)

    data["ATR"] = true_range.rolling(14).mean()
    return data
def calculate_volatility(data):
    """
    Calculates annualized volatility of a stock.

    Parameters:
       the data (DataFrame)

    Returns:
       a float
    """
    volatility =data["Daily Return"].std() * np.sqrt(252)#here we calculate the volatility using the standard deviation and we are multiplying it to
    #the squareroot of 252 becase the 252=252 trading days
    #therefore when we multiply it with 252 we get annual volatility
    return volatility
