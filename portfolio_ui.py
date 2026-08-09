import streamlit as st
from comparison import compare_stocks
from portfolio import (
    generate_portfolio,
    portfolio_chart,
    get_portfolio_returns
)
from portfolio_ai import explain_portfolio

def show_portfolio():
    st.title("💼 AI Portfolio Builder")
    investment = st.number_input(
        "Investment Amount (₹)",
        min_value=1000,
        value=100000,
        step=1000
    )
    risk_preference = st.selectbox(
        "Risk Appetite",
        [
            "Low",
            "Medium",
            "High"
        ]
    )
    portfolio_list = st.multiselect(
        "Portfolio Stocks",
        ["AAPL","MSFT","NVDA","GOOGL","META","AMZN","TSLA",
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
                    "ICICIPRULI.NS"
        ]
    
    )
    if st.button("Generate Portfolio"):
        comparison_df = compare_stocks(portfolio_list)
        portfolio_df = generate_portfolio(
            comparison_df,
            investment,
            risk_preference
        )
        st.dataframe(
            portfolio_df,
            use_container_width=True
        )
        portfolio_explanation = explain_portfolio(
                    portfolio_df,
                    risk_preference
                )
        st.subheader("🤖 AI Portfolio Explanation")

        st.info("\n\n".join(portfolio_explanation))
        fig = portfolio_chart(portfolio_df)
        if fig:
            st.plotly_chart(
                fig,
                use_container_width=True
            )
        st.success(
            f"Total Investment: ₹{portfolio_df['Investment (₹)'].sum():,.0f}"
        )
        