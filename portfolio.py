import pandas as pd
import numpy as np
from portfolio_optimizer import (
    generate_random_portfolios,
    plot_efficient_frontier,
    get_best_portfolio
)
def generate_portfolio(comparison_df, investment, risk_preference):
    if comparison_df.empty:
        return pd.DataFrame()
#filter using the risk preference
    if risk_preference == "Low":

        comparison_df = comparison_df[
            comparison_df["Risk"] == "🟢 Low Risk"
        ]
    elif risk_preference == "Medium":
        comparison_df = comparison_df[
            comparison_df["Risk"].isin(
                [
                    "🟢 Low Risk",
                    "🟡 Medium Risk"
                ]
            )
        ]
    selected = comparison_df[
        comparison_df["Recommendation"].isin(
            [
                "🟢 BUY",
                "🟢 STRONG BUY"
            ]
        )
    ].copy()
    # If none qualify, use Top 5
    if selected.empty:
        selected = comparison_df.sort_values(
            by="Score",
            ascending=False
        ).head(5)

#teh best stocks per sector
    if "Sector" in selected.columns:
        selected = (
            selected
            .sort_values(
                by="Score",
                ascending=False
            )
            .drop_duplicates(
                subset="Sector"
            )
        )
#portfolio alloctaion
    total_score = selected["Score"].sum()
    selected["Weight (%)"] = (
        selected["Score"] / total_score
    ) * 100
    selected["Investment (₹)"] = (
        selected["Weight (%)"] / 100
    ) * investment
    return selected[
        [
            "Ticker",
            "Score",
            "Recommendation",
            "Weight (%)",
            "Investment (₹)"
        ]
    ]
import plotly.express as px
def portfolio_chart(portfolio_df):
    if portfolio_df.empty:
        return None
    fig = px.pie(
        portfolio_df,
        names="Ticker",
        values="Investment (₹)",
        title="Portfolio Allocation"
    )
    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )
    fig.update_layout(
        legend_title="Stocks"
    )
    return fig
import yfinance as yf
def get_portfolio_returns(stocks):
    price_data = pd.DataFrame()
    for stock in stocks:
        try:
            data = yf.download(
                stock,
                period="1y",
                progress=False,
                auto_adjust=True
            )
            if not data.empty:
                price_data[stock] = data["Close"]
        except:
            continue
    if price_data.empty:
        return pd.DataFrame()
    returns = price_data.pct_change().dropna()
    return returns