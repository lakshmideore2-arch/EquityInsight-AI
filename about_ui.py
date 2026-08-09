import streamlit as st
def show_about():
    st.title("ℹ️ About EquityInsight AI")
    st.markdown("""
## 📈 EquityInsight AI
EquityInsight AI is an AI-powered investment analysis platform built using Python and Streamlit.
The application combines:
- 📈 Technical Analysis
- 📰 News Sentiment Analysis
- 🤖 AI Investment Thesis
- 💼 AI Portfolio Builder
- ⚖️ Stock Comparison
- 📊 Market Watch
- 📄 Financial Statements
- 📑 PDF Report Generation
to help investors make informed decisions.
""")
    st.divider()
    st.subheader("🛠️ Technologies Used")
    st.markdown("""
- Python
- Streamlit
- yFinance
- Pandas
- NumPy
- Plotly
- ReportLab
- BeautifulSoup
- Requests
 🎯 Project Objective
EquityInsight AI was developed to demonstrate the practical application of **Artificial Intelligence, Quantitative Finance, Financial Analytics, and Data Science** in a unified investment research platform.
The platform integrates multiple analytical techniques to generate intelligent investment recommendations, quantitative risk assessments, portfolio analytics, and automated investment reports.
""")
    st.divider()
    st.subheader("👩‍💻 About the Developer")

    st.markdown("""
    ### Lakshmi Atul Deore

    **B.Sc. Applied Statistics & Data Science**  
    Symbiosis Statistical Institute

    **B.A. Economics**  
    Ramakrishna More Autonomous College of Arts, Commerce & Science

    I am interested in the intersection of **Economics, Statistics, Data Science, and Finance**,
    with a particular focus on quantitative analysis, financial markets, and data-driven decision-making.

    **EquityInsight AI** was developed as an independent project to explore how statistical
    methods, financial analysis, quantitative modelling, and AI can be integrated into a
    single investment research workflow.
    """)
    st.divider()
    st.subheader("⚠️ Disclaimer")
    st.info(
        "This application is developed solely for educational and research purposes." \
     
        "It does not constitute financial or investment advice. Users should conduct their own research before making investment decisions."
        
    )
    st.markdown("""
### 🔗 Connect

**GitHub:** https://github.com/lakshmideore2-arch
""")