import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import streamlit as st
def display_report(company_info,
                   ticker,
                   stock_data,
                   adjusted_score,
                   recommendation,
                   explanation,
                   risk,
                   confidence,
                   reasons,
                   news_summary,
                   news,
                   levels,
                   alerts,
                   patterns,
                   trend_explanation,
                   fundamentals,
                   thesis,
                   strengths,
                   weaknesses
                   ):
    from live_price import get_live_price
    current_price = get_live_price(ticker)
    if current_price is None:
        current_price = stock_data["Close"].iloc[-1]
    st.header("Investment Report")
    #comapny's information
    with st.expander("🏢 Company Information", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Company:** {company_info['Name']}")
            st.write(f"**Ticker:** {ticker}")
            st.write(f"**Sector:** {company_info['Sector']}")

        with col2:
            st.write(f"**Industry:** {company_info['Industry']}")
            st.write(f"**Country:** {company_info['Country']}")
            st.write(f"**Current Price:** ₹{current_price:.2f}")

        st.divider()
    with  st.expander("📑 Company Fundamentals", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Market Cap", fundamentals.get("Market Cap", "N/A"))
            st.metric("PE Ratio", fundamentals.get("PE Ratio", "N/A"))
            st.metric("Forward PE", fundamentals.get("Forward PE", "N/A"))
        with col2:
            st.metric("EPS", fundamentals.get("EPS", "N/A"))
            st.metric("Book Value", fundamentals.get("Book Value", "N/A"))
            st.metric("Dividend Yield", fundamentals.get("Dividend Yield", "N/A"))
        with col3:
            st.metric("Beta", fundamentals.get("Beta", "N/A"))
            st.metric("Profit Margin", fundamentals.get("Profit Margin", "N/A"))
            st.metric("ROE", fundamentals.get("Return on Equity", "N/A"))
        st.divider()
    with st.expander("Ai Investment Thesis",expanded=True):
        st.markdown("""
        <div style="
            background-color:#1E1E1E;
            padding:20px;
            border-radius:12px;
            border-left:6px solid #4CAF50;
        ">
        """, unsafe_allow_html=True)
        st.markdown(thesis)
        st.markdown("</div>", unsafe_allow_html=True)
        st.divider()
#Executive summary
        st.subheader(" Executive Summary")
        col1, col2, col3,col4 = st.columns(4)
        col1.metric("Score", f"{adjusted_score}/100")
        col2.metric("Risk", risk)
        col3.metric("Recommendation", recommendation)
        col4.metric("Confidence",f"{confidence}%")
        st.divider()
    
    with st.expander("🚨 AI Watchlist Alerts", expanded=True):
        for alert in alerts:
            st.write(alert)
        st.subheader("📈 Market Trend")
        st.write(trend_explanation)
        st.subheader("📍 Support & Resistance")
        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                "Support",
                f"₹{levels['Support']}"
            )
            st.metric(
                "Downside Risk",
                f"{levels['Downside']}%"
            )
        
        with col2:
            st.metric(
                "Resistance",
                f"₹{levels['Resistance']}"
            )

            st.metric(
                "Upside Potential",
                f"{levels['Upside']}%"
            )
        #technicla indicators
            st.divider()
        st.expander("📈 Reasons Behind Recommendation")
        for reason in reasons:
            st.write(f"✔ {reason}")
        st.divider()
#the news sentiments

    with st.expander("📰 News Sentiment", expanded=True):

        st.write(f"Positive : {news_summary['Positive']}")
        st.write(f"Neutral : {news_summary['Neutral']}")
        st.write(f"Negative : {news_summary['Negative']}")
        st.write(f"Overall : {news_summary['Overall']}")

        st.divider()

    with st.expander("📰 Latest News", expanded=True):

        for article in news:

            st.markdown(f"**{article['title']}**")

            if article.get("published date"):
                st.caption(article["published date"])

            st.write("")
 # Disclaimer
        st.divider()
    with st.expander("🟢 Strengths", expanded=True):
        for item in strengths:
            st.success(item)
        st.divider()
    with st.expander("🔴 Weaknesses",expanded=True):
        for item in weaknesses:
            st.warning(item)
        st.info(
            "This recommendation is based on technical indicators "
            "and recent news sentiment. "
            "It should not be considered financial advice. "
            "Always conduct your own research before investing."
        )
        st.subheader("🕯️ Candlestick Patterns")
        if patterns:
            for name, meaning in patterns:
                st.success(name)
                st.write(meaning)
        else:
            st.write("No major pattern detected today.")