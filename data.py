import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

@st.cache_data(ttl=60,show_spinner=False)
def get_stock_data(
    ticker,
    period="1y",
    interval="1d"
):
    with st.spinner("Getting the Stock Data"):
        stock = yf.Ticker(ticker)
        data = stock.history(
            period=period,
            interval=interval
        )
        if data.empty:
            return None
        return data


@st.cache_data(ttl=86400,show_spinner=False)
def get_company_info(ticker):
    """
    Fetch company information using yfinance.
    """
    with st.spinner("Getting the Company Info"):
        stock = yf.Ticker(ticker)

        info = stock.info

        company = {
            "Name": info.get("longName", "Not Available"),
        "Sector": info.get("sector", "Not Available"),
        "Industry": info.get("industry", "Not Available"),
        "Country": info.get("country", "Not Available"),
        "Currency": info.get("currency", "Not Available"),
        "Current Price": info.get("currentPrice", "N/A"),
        "Previous Close": info.get("previousClose", "N/A"),
        "Open": info.get("open", "N/A"),
        "Day High": info.get("dayHigh", "N/A"),
        "Day Low": info.get("dayLow", "N/A"),
        "Market Cap": info.get("marketCap", "N/A"),
        "Volume": info.get("volume", "N/A"),
        "Average Volume": info.get("averageVolume", "N/A"),
        "PE Ratio": info.get("trailingPE", "N/A"),
        "Forward PE": info.get("forwardPE", "N/A"),
        "Book Value": info.get("bookValue", "N/A"),
        "EPS": info.get("trailingEps", "N/A"),
        "Beta": info.get("beta", "N/A"),
        "Dividend Yield": info.get("dividendYield", "N/A"),
        "52 Week High": info.get("fiftyTwoWeekHigh", "N/A"),
        "52 Week Low": info.get("fiftyTwoWeekLow", "N/A")
        }

        return company
@st.cache_data(ttl=86400,show_spinner=False)
def get_fundamentals(ticker):
    with st.spinner("Getting the fundamenatals"):
        stock = yf.Ticker(ticker)#downloading tyhe stock data 
        info = stock.info
        fundamentals = {#buildidng our own dicytionary 
            "Market Cap": info.get("marketCap"),
            "PE Ratio": info.get("trailingPE"),
            "Forward PE": info.get("forwardPE"),
            "EPS": info.get("trailingEps"),
            "Book Value": info.get("bookValue"),
            "Dividend Yield": info.get("dividendYield"),
            "Beta": info.get("beta"),
            "Profit Margin": info.get("profitMargins"),
            "Return on Equity": info.get("returnOnEquity")
        }
        return fundamentals
#getting tyeh financial statement 
@st.cache_data(ttl=86400,show_spinner=False)
def get_financial_statements(ticker):
    with st.spinner("Getting the financial statements"):
        stock = yf.Ticker(ticker)
        income = stock.financials#downloads teh income stattement 
        balance = stock.balance_sheet #gives tyhe balance sheet 
        cashflow = stock.cashflow#gettting tyhe cashflow
        return income, balance, cashflow
def timeframe_settings(timeframe):
    mapping = {
        "1 Minute": ("7d", "1m"),
        "3 Minutes": ("60d", "5m"),
        "5 Minutes": ("60d", "5m"),
        "15 Minutes": ("60d", "15m"),
        "30 Minutes": ("60d", "30m"),
        "1 Hour": ("730d", "1h"),
        "1 Day": ("1y", "1d"),
        "1 Week": ("5y", "1wk"),
        "1 Month": ("10y", "1mo")
    }
    return mapping[timeframe]