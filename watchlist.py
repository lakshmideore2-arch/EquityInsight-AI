import yfinance as yf
import pandas as pd
import streamlit as st
import traceback
from indicators import (
    calculate_indicators,
    calculate_volatility
)
from scoring import (
    calculate_score,
    generate_recommendation,
    risk_level
)
@st.cache_data(ttl=60,show_spinner=False)
def get_watchlist():
    with st.spinner("Getting the Market Watch Data"):
        tickers = [
                "AAPL","MSFT","NVDA","GOOGL","META","AMZN","TSLA",
                "AMD","NFLX","INTC","ORCL","IBM","ADBE","CRM",
                # India
                "RELIANCE.NS",
                "TCS.NS",
                "INFY.NS",
                "HDFCBANK.NS",
                "ICICIBANK.NS",
                "SBIN.NS",
                "LT.NS",
                "ITC.NS",
                "HINDUNILVR.NS",
                "BHARTIARTL.NS",
                "ASIANPAINT.NS",
                "TITAN.NS",
                "MARUTI.NS",
                "AXISBANK.NS",
                "BAJFINANCE.NS",
                "SUNPHARMA.NS",
                # Banking & Financials
                "KOTAKBANK.NS",
                "INDUSINDBK.NS",
                "BANKBARODA.NS",
                "PNB.NS",
                "CANBK.NS",
                "IDFCFIRSTB.NS",
                # Information Technology
                "HCLTECH.NS",
                "TECHM.NS",
                "WIPRO.NS",
                "PERSISTENT.NS",
                "LTIM.NS",
                # Automobile
                "TATAMOTORS.NS",
                "M&M.NS",
                "EICHERMOT.NS",
                "HEROMOTOCO.NS",
                "BAJAJ-AUTO.NS",
                # FMCG
                "NESTLEIND.NS",
                "BRITANNIA.NS",
                "DABUR.NS",
                "GODREJCP.NS",
                "MARICO.NS",
                # Pharmaceuticals & Healthcare
                "CIPLA.NS",
                "DRREDDY.NS",
                "DIVISLAB.NS",
                "LUPIN.NS",
                "APOLLOHOSP.NS",
                # Energy & Utilities
                "POWERGRID.NS",
                "NTPC.NS",
                "ONGC.NS",
                "COALINDIA.NS",
                "BPCL.NS",
                "IOC.NS",
                # Metals & Mining
                "TATASTEEL.NS",
                "JSWSTEEL.NS",
                "HINDALCO.NS",
                "VEDL.NS",
                # Cement & Construction
                "ULTRACEMCO.NS",
                "GRASIM.NS",
                "SHREECEM.NS",
                # Telecom & Media
                "BHARTIARTL.NS",
                "TATACOMM.NS",
                # Adani Group
                "ADANIENT.NS",
                "ADANIPORTS.NS",
                # Consumer & Retail
                "DMART.NS",
                "TRENT.NS",
                # Chemicals & Paints
                "PIDILITIND.NS",
                "BERGEPAINT.NS",
                # Insurance
                "SBILIFE.NS",
                "HDFCLIFE.NS",
                "ICICIPRULI.NS"]
        watchlist = []
        for ticker in tickers:
            try:
                print("Downloading:", ticker)
                stock = yf.Ticker(ticker)
                data = yf.download(
                tickers=ticker,
                period="1y",
                auto_adjust=False,
                progress=False,
                group_by="column"
            )
                # Convert MultiIndex columns to normal columns
                if isinstance(data.columns, pd.MultiIndex):
                    data.columns = data.columns.get_level_values(0)
                if data.empty:
                    continue
                # Remove incomplete trading day
                data = data.dropna(subset=["Close"])
                if len(data) < 2:
                    continue
                data = calculate_indicators(data)          
                volatility = calculate_volatility(data)
                score, reasons, yearly_return = calculate_score(
                    data,
                    volatility
                )
                recommendation, explanation = generate_recommendation(score)
                risk, risk_explanation = risk_level(volatility)
                from live_price import get_live_price
                current = get_live_price(ticker)
                if current is None:
                    current = float(data["Close"].iloc[-1])
                previous = data["Close"].iloc[-2]
                change = ((current - previous) / previous) * 100
                if change > 0:
                    trend = "Bullish"
                else:
                    trend="Bearish"
                print("Adding:", ticker)
                watchlist.append({
                    "Ticker": ticker,
                    "Price": round(current, 2),
                    "Change %": round(change, 2),
                    "Trend": trend,
                    "Score": score,
                    "Recommendation": recommendation,
                    "Risk": risk
                })
                print("Total stocks:", len(watchlist))
            except Exception as e:
                traceback.print_exc()
        return pd.DataFrame(watchlist)  
@st.cache_data(ttl=60,show_spinner=False)
def get_top_gainers(watchlist):
    with st.spinner("Getting the top gainers"):
        return (
            watchlist
            .sort_values(
                by="Change %",
                ascending=False
            )
            .head(5)
        )
@st.cache_data(ttl=60,show_spinner=False)
def get_top_losers(watchlist):
    with st.spinner("Getting the top losers"):
        return (
            watchlist
            .sort_values(
                by="Change %"
            )
            .head(5)
        )