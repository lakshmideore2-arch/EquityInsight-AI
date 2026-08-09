import streamlit as st
print("Loading market_watch_ui...")
from market import get_market_overview
from watchlist import (
    get_watchlist,
    get_top_gainers,
    get_top_losers)

def show_market_watch():
    market = get_market_overview()
    st.subheader("MARKET OVERVIEW")
    if market:
        cols = st.columns(len(market))
        for col,(name,info) in zip(cols,market.items()):
            with col:
                if info ["Trend"]=="Bullish":
                    emoji = "🟢"
                elif info["Trend"]=="Bearish":
                    emoji = "🔴"
                else:
                    emoji = "🟡"
                st.metric(
                    label=f"{emoji} {name}",
                    value=f"{info['Current']:,.2f}",
                    delta=f"{info['Change']}%"
                )
    else:
        st.warning("Market overview is currently unavailable.")
    watchlist = get_watchlist()
    st.subheader("Market watch")
    for _, stock in watchlist.iterrows():
        col1,col2,col3,col4=st.columns([1,1,1,2])#with the last column being much wider
        with col1:
            st.write(f"**{stock['Ticker']}**")
        with col2:
            st.write(f"**{stock['Price']}**")
        with col3:
            if stock["Trend"]=="Bullish":
                st.success(stock["Trend"])
            else:
                st.error(stock['Trend'])
        with col4:
            st.write(f"**{stock['Recommendation']}**")
    st.divider()#adds an horizontal line 
