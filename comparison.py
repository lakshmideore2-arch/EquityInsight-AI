import pandas as pd
import plotly.graph_objects as go
from data import get_company_info
from data import (
    get_stock_data,
    get_fundamentals
)
from indicators import (
    calculate_indicators,
    calculate_volatility
)
from scoring import (
    calculate_score,
    generate_recommendation,
    risk_level
)
from live_price import get_live_price
def compare_stocks(tickers):
    comparison = []
    for ticker in tickers:
        try:
            data = get_stock_data(ticker)
            company=get_company_info(ticker)
            if data.empty:
                continue
            data = calculate_indicators(data)
            volatility = calculate_volatility(data)
            score, _, _ = calculate_score(
                data,
                volatility
            )
            recommendation, _ = generate_recommendation(score)
            risk, _ = risk_level(volatility)
            fundamentals = get_fundamentals(ticker)
            live_price = get_live_price(ticker)
            if live_price is None:
                live_price = float(data["Close"].iloc[-1])
            comparison.append({
                "Ticker": ticker,
                "Price":round(live_price,2),
                "Score": score,
                "Risk": risk,
                "Recommendation": recommendation,
                "Sector": company["Sector"],
                "PE Ratio": fundamentals["PE Ratio"],
                "ROE": fundamentals["Return on Equity"]})
        except Exception as e :
             print(f"Error while comparing {ticker}: {e}")
             continue
    return pd.DataFrame(comparison)
def comparison_chart(tickers):
    fig = go.Figure()
    for ticker in tickers:
        data = get_stock_data(
            ticker,
            period="6mo",
            interval="1d"
        )
        if data is None or data.empty:
            continue
        normalized = (
            data["Close"] /
            data["Close"].iloc[0]
        ) * 100
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=normalized,
                mode="lines",
                name=ticker
            )
        )
    fig.update_layout(
        title="6 Month Stock Performance Comparison",
        xaxis_title="Date",
        yaxis_title="Performance (Base = 100)",
        template="plotly_white"
    )
    return fig
def ai_compare_verdict(comparison_df):
    if comparison_df.empty:
        return "No stocks available for comparison."
    # Highest score wins
    best_stock = comparison_df.sort_values(
        by="Score",
        ascending=False
    ).iloc[0]
    verdict = (
        f"🏆 **{best_stock['Ticker']}** appears to be the strongest "
        f"investment among the selected stocks.\n\n"
        f"### Why?\n"
        f"- Technical Score: **{best_stock['Score']}/100**\n"
        f"- Recommendation: **{best_stock['Recommendation']}**\n"
        f"- Risk Level: **{best_stock['Risk']}**\n"
        f"- PE Ratio: **{best_stock['PE Ratio']}**\n"
        f"- ROE: **{best_stock['ROE']}**\n\n"
        "Overall, this stock currently offers the strongest combination "
        "of technical strength, profitability, and investment quality."
    )
    return verdict
