import numpy as np
import pandas as pd
def monte_carlo_simulation(
    stock_data,
    days=252,
    simulations=1000
):
    """
    Simulates future stock prices using
    Geometric Brownian Motion.
    """
    close = stock_data["Close"]
    daily_returns = close.pct_change().dropna()
    mu = daily_returns.mean()
    sigma = daily_returns.std()#daily volatility
    last_price = close.iloc[-1]
    simulated_prices = np.zeros((days, simulations))
    simulated_prices[0] = last_price
 #monte carlo simulation
    for sim in range(simulations):
        for day in range(1, days):
            random_shock = np.random.normal()
            simulated_prices[day, sim] = (
                simulated_prices[day - 1, sim]
                * np.exp(
                    (mu - 0.5 * sigma**2)
                    + sigma * random_shock
                )
            )
    return (
        simulated_prices,
        mu,
        sigma
    )
import plotly.graph_objects as go

def plot_monte_carlo(simulated_prices):
    """
    Plot Monte Carlo simulation paths.
    """
    fig = go.Figure()
    # Display only the first 100 simulations for clarity
    num_paths = min(100, simulated_prices.shape[1])
    for i in range(num_paths):
        fig.add_trace(
            go.Scatter(
                x=np.arange(simulated_prices.shape[0]),
                y=simulated_prices[:, i],
                mode="lines",
                line=dict(width=1),
                opacity=0.3,
                showlegend=False
            )
        )
    fig.update_layout(
        title="Monte Carlo Stock Price Simulation",
        xaxis_title="Trading Days",
        yaxis_title="Simulated Price",
        template="plotly_dark",
        height=650
    )
    return fig
def monte_carlo_statistics(
    simulated_prices,
    current_price
):
    """
    Calculate risk statistics from
    Monte Carlo simulation.
    """
    final_prices = simulated_prices[-1]
    expected_price = np.mean(final_prices)
    probability_profit = (
        np.sum(final_prices > current_price)
        / len(final_prices)
    ) * 100
    lower_bound = np.percentile(
        final_prices,
        2.5
    )
    upper_bound = np.percentile(
        final_prices,
        97.5
    )
    best_case = np.max(final_prices)
    worst_case = np.min(final_prices)
    return {
        "Expected Price": expected_price,
        "Probability of Profit": probability_profit,
        "Lower CI": lower_bound,
        "Upper CI": upper_bound,
        "Best Case": best_case,
        "Worst Case": worst_case
    }