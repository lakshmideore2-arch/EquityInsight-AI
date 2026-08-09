import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def analyze_technical_signals(stock_data):
    """
    Analyzes all technical indicators and returns
    bullish/bearish signals.
    """
    signals = []
    bullish = 0
    bearish = 0
    latest = stock_data.iloc[-1]

    price = latest["Close"]
    # Moving Averages
    if price > latest["MA20"]:
        bullish += 1
        signals.append("✅ Price is above MA20 (Short-term Bullish)")
    else:
        bearish += 1
        signals.append("❌ Price is below MA20")
    if price > latest["MA50"]:
        bullish += 1
        signals.append("✅ Price is above MA50 (Medium-term Bullish)")
    else:
        bearish += 1
        signals.append("❌ Price is below MA50")

    if price > latest["MA200"]:
        bullish += 2
        signals.append("✅ Price is above MA200 (Long-term Bullish)")
    else:
        bearish += 2
        signals.append("❌ Price is below MA200")
    # EMA
    if latest["EMA20"] > latest["EMA50"]:
        bullish += 1
        signals.append("✅ EMA20 is above EMA50")
    else:
        bearish += 1
        signals.append("❌ EMA20 is below EMA50")
    # RSI
    if latest["RSI"] < 30:
        bullish += 1
        signals.append("🟢 RSI indicates Oversold")
    elif latest["RSI"] > 70:
        bearish += 1
        signals.append("🔴 RSI indicates Overbought")
    else:
        signals.append("🟡 RSI is Neutral")
    # MACD
    if latest["MACD"] > latest["Signal"]:
        bullish += 2
        signals.append("✅ MACD Bullish Crossover")
    else:
        bearish += 2
        signals.append("❌ MACD Bearish Crossover")
    # Bollinger Bands
    if price > latest["Upper Band"]:
        bearish += 1
        signals.append("🔴 Price above Upper Bollinger Band")
    elif price < latest["Lower Band"]:
        bullish += 1
        signals.append("🟢 Price below Lower Bollinger Band")
    # Final Trend
    if bullish > bearish:
        trend = "🟢 Bullish"
    elif bearish > bullish:
        trend = "🔴 Bearish"
    else:

        trend = "🟡 Sideways"
    bullish_percent = round((bullish / 9) * 100)
    bearish_percent = round((bearish / 9) * 100)
    return {
        "Trend": trend,
        "Bullish Signals": bullish,
        "Bearish Signals": bearish,
        "Bullish %": bullish_percent,
        "Bearish %": bearish_percent,
        "Signals": signals
    }