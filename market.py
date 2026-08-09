import yfinance as yf
import streamlit as st
@st.cache_data(ttl=60,show_spinner=False)
def get_market_overview():
    with st.spinner("Getting the Market Overview"):
        indices = {
            "NIFTY 50": "^NSEI",
            "SENSEX": "^BSESN",
            "S&P 500": "^GSPC",
            "NASDAQ": "^IXIC",
            "GOLD": "GC=F",
            "BITCOIN": "BTC-USD"
        }
        market = {}
        for name, symbol in indices.items():
            try:
                stock = yf.Ticker(symbol)
                data = stock.history(period="5d")
                if data.empty or len(data) < 2:
                    continue
                current = float(data["Close"].iloc[-1])
                previous = float(data["Close"].iloc[-2])
                change = ((current - previous) / previous) * 100
                if change > 0.5:
                    trend = "Bullish"
                elif change < -0.5:
                    trend = "Bearish"
                else:
                    trend = "Sideways"
                market[name] = {
                    "Current": round(current, 2),
                    "Change": round(change, 2),
                    "Trend": trend
                }
            except  Exception as e:
                print(name, e)
        print(market)
        return market
