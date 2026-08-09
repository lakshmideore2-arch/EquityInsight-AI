import streamlit as st
def show_comparison():
    comparison_list = st.multiselect(
        "Compare Stocks",
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
    compare = st.button("📊 Compare Stocks")
    from comparison import (
        compare_stocks,
        comparison_chart,
        ai_compare_verdict
    )
    if compare:
        if len(comparison_list) < 2:
            st.warning("Please select at least 2 stocks.")
            st.stop()
        comparison_df = compare_stocks(comparison_list)
        fig = comparison_chart(comparison_list)
        st.plotly_chart(
            fig,
            use_container_width=True
        )
        st.header("📊 Stock Comparison")
        st.divider()
        st.subheader("🤖 AI Comparison Verdict")
        verdict = ai_compare_verdict(comparison_df)
        st.info(verdict)
        st.dataframe(comparison_df)