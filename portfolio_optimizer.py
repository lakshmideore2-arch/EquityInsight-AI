import numpy as np
import pandas as pd
def calculate_portfolio_statistics(weights, returns):
    #calculating the expected returns
    mean_returns = returns.mean() * 252#avg * 252 trading days
    covariance = returns.cov() * 252#how the stocks are moving 
    portfolio_return = np.sum(
        mean_returns * weights
    )

    portfolio_volatility = np.sqrt(
        np.dot(
            weights.T,
            np.dot(covariance, weights)
        )
    )
    return portfolio_return, portfolio_volatility
def generate_random_portfolios(
    returns,
    num_portfolios=5000):
    #generating random portfolios and calculating teh return , volatility and sharperatio
    num_assets = returns.shape[1]
    results = []
    weights_list = []
    for _ in range(num_portfolios):
        # Generate random weights
        weights = np.random.random(num_assets)
        # Make weights sum to 1
        weights /= np.sum(weights)
        portfolio_return, portfolio_volatility = (
            calculate_portfolio_statistics(
                weights,
                returns
            )
        )
    
        sharpe_ratio = (
            portfolio_return / portfolio_volatility
            if portfolio_volatility > 0
            else 0
        )
        results.append([
            portfolio_return,
            portfolio_volatility,
            sharpe_ratio
        ])
        weights_list.append(weights)
    results = np.array(results)
    return results, weights_list
import plotly.graph_objects as go
def plot_efficient_frontier(results):
   #ploting teh efficient frointeir"
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=results[:, 1],      # Volatility
            y=results[:, 0],      # Return
            mode="markers",
            marker=dict(
                size=6,
                color=results[:, 2],   # Sharpe Ratio
                colorscale="Viridis",
                colorbar=dict(title="Sharpe Ratio")
            ),
            name="Random Portfolios"
        )
    )
    fig.update_layout(
        title="Efficient Frontier",
        xaxis_title="Portfolio Volatility (Risk)",
        yaxis_title="Expected Annual Return",
        template="plotly_dark",
        height=650
    )
    return fig
def get_best_portfolio(
    results,
    weights_list
):
    """
    Returns the portfolio with
    the highest Sharpe Ratio.
    """
    best_index = np.argmax(results[:, 2])
    return {
        "Return": results[best_index, 0],
        "Volatility": results[best_index, 1],
        "Sharpe": results[best_index, 2],
        "Weights": weights_list[best_index]
    }