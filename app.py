import streamlit as st
from portfolio_ui import show_portfolio

from comparison_ui import show_comparison
from market_watch_ui import show_market_watch
from about_ui import show_about
from analysis_ui import show_analysis
st.set_page_config(
    page_title="EquityInsight AI",
    page_icon="📈",
    layout="wide"
)

page = st.sidebar.radio(
    "📌 Navigation",
    [
        "🏠 Home",
        "📊 Market Watch",
        "📈 Stock Analysis",
        "💼 Portfolio Builder",
        "⚖️ Compare Stocks",
        "ℹ️ About"
    ]
)

if page == "🏠 Home":

    st.title("📈 EquityInsight AI")

    st.markdown("""
## Welcome to EquityInsight AI

An AI-powered quantitative investment research platform designed to integrate financial data, statistical analysis, risk modelling and AI-assisted investment insights.

### Features

- 📈 Stock Analysis
- 🤖 AI Investment Thesis
- 💬 AI Assistant
- 💼 Portfolio Builder
- ⚖️ Stock Comparison
- 📊 Market Watch
- 📄 Financial Statements
- 📑 PDF Report Generation

---

👈 Select a feature from the navigation menu.
""")
import streamlit as st

# Initialize session state variables
if "committee_decision" not in st.session_state:
    st.session_state.committee_decision = []

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

elif page == "📊 Market Watch":
    show_market_watch()

elif page == "📈 Stock Analysis":
    show_analysis()

elif page == "💼 Portfolio Builder":

    show_portfolio()

elif page == "⚖️ Compare Stocks":

    show_comparison()

elif page == "ℹ️ About":

    show_about()