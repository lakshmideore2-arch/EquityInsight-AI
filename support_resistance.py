import numpy as np
import streamlit as st 
@st.cache_data(ttl=60,show_spinner=False)
def calculate_support_resistance(stock_data):
    with st.spinner("Calculating teh support resistance"):
        recent_data = stock_data.tail(60)
        resistance = recent_data["High"].max()
        support = recent_data["Low"].min()
        current_price = stock_data["Close"].iloc[-1]
        upside = ((resistance - current_price) / current_price) * 100
        downside = ((current_price - support) / current_price) * 100
        return {
            "Support": round(support, 2),
            "Resistance": round(resistance, 2),
            "Current Price": round(current_price, 2),
            "Upside": round(upside, 2),
            "Downside": round(downside, 2)
        }