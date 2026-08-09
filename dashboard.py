import streamlit as st
def technical_dashboard(analysis):

    st.header("📊 Technical Analysis Dashboard")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "Market Trend",
            analysis["Trend"]
        )
    with col2:
        st.metric(
        "🐂 Bullish Score",
        f"{analysis['Bullish Signals']}/9"
    )
    with col3:
        st.metric(
        "🐻 Bearish Score",
       f"{analysis['Bearish Signals']}/9"
    )
    st.divider()
    st.subheader("Indicator Signals")
    for signal in analysis["Signals"]:
        st.write(signal)