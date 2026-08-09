import pandas as pd
import streamlit as st 
@st.cache_data(ttl=60,show_spinner=False)
def detect_patterns(data):
    with st.spinner("Detecting the patterns"):
        patterns = []
        latest = data.iloc[-1]
        previous = data.iloc[-2]
        body = abs(latest["Close"] - latest["Open"])
        candle_range = latest["High"] - latest["Low"]
        upper_shadow = latest["High"] - max(
            latest["Open"],
            latest["Close"]
        )
        lower_shadow = min(
            latest["Open"],
            latest["Close"]
        ) - latest["Low"]
        # Doji

        if body <= candle_range * 0.1:

            patterns.append(
                (
                    "⚪ Doji",
                    "Market indecision."
                )
            )

# Hammer


        if lower_shadow > body * 2 and upper_shadow < body:

            patterns.append(
                (
                    "🟢 Hammer",
                    "Possible bullish reversal."
                )
            )
        # Shooting Star

        if upper_shadow > body * 2 and lower_shadow < body:
            patterns.append(
                (
                    "🔴 Shooting Star",
                    "Possible bearish reversal."
                )
            )
        # Bullish Engulfing
        if (
            previous["Close"] < previous["Open"]
            and
            latest["Close"] > latest["Open"]
            and
            latest["Open"] < previous["Close"]
            and
            latest["Close"] > previous["Open"]
        ):
            patterns.append(
                (
                    "🟢 Bullish Engulfing",
                    "Strong buying pressure."
                )
            )
        # Bearish Engulfing
        if (
            previous["Close"] > previous["Open"]
            and
            latest["Close"] < latest["Open"]
            and
            latest["Open"] > previous["Close"]
            and
            latest["Close"] < previous["Open"]
        ):
            patterns.append(
                (
                    "🔴 Bearish Engulfing",
                    "Strong selling pressure."
                )
            )
        return patterns