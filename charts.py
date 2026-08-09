import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import streamlit as st 
@st.cache_data(ttl=60,show_spinner=False)
def plot_dashboard(stock_data, company_name):
    with st.spinner("Plotting the graphs"):
        fig = make_subplots(
            rows=3,
            cols=1,
            shared_xaxes=True,
            vertical_spacing=0.04,
            row_heights=[0.6, 0.2, 0.2],
            subplot_titles=(
                "Price & Moving Averages",
                "RSI",
                "MACD"
            )
        )
        fig.add_trace(
        go.Candlestick(
            x=stock_data.index,
            open=stock_data["Open"],
            high=stock_data["High"],
            low=stock_data["Low"],
            close=stock_data["Close"],
            name="Price"
        ),
        row=1,
        col=1
    )
        fig.add_trace(
        go.Scatter(
            x=stock_data.index,
            y=stock_data["MA20"],
            mode="lines",
            name="MA20"
        ),
        row=1,
        col=1
    )
        fig.add_trace(
        go.Scatter(
            x=stock_data.index,
            y=stock_data["MA50"],
            mode="lines",
            name="MA50"
        ),
        row=1,
        col=1
    )
        fig.add_trace(
        go.Scatter(
            x=stock_data.index,
            y=stock_data["MA200"],
            mode="lines",
            name="MA200"
        ),
        row=1,
        col=1
    )
        fig.add_trace(
        go.Scatter(
            x=stock_data.index,
            y=stock_data["RSI"],
            mode="lines",
            name="RSI"
        ),
        row=2,
        col=1
    )
        fig.add_hline(
        y=70,
        line_dash="dash",
        line_color="red",
        row=2,
        col=1
    )


        fig.add_hline(
            y=30,
            line_dash="dash",
            line_color="green",
            row=2,
            col=1
    )
        fig.add_trace(
        go.Scatter(
            x=stock_data.index,
            y=stock_data["MACD"],
            mode="lines",
            name="MACD"
        ),
        row=3,
        col=1
    )
        fig.add_trace(
        go.Scatter(
            x=stock_data.index,
            y=stock_data["Signal"],
            mode="lines",
            name="Signal"
        ),
        row=3,
        col=1
    )
        histogram = stock_data["MACD"] - stock_data["Signal"]

        fig.add_trace(
            go.Bar(
                x=stock_data.index,
                y=histogram,
                name="Histogram"
            ),
            row=3,
            col=1
    )
        fig.update_layout(
        title=f"{company_name} Technical Analysis Dashboard",
        template="plotly_white",
        xaxis_title="Date",
        yaxis_title="Price",
        height=900,
        hovermode="x unified",
        xaxis_rangeslider_visible=False,
        showlegend=True
    )  
        return fig
