import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def risk_level(volatility):
    if volatility < 20:
        return (
            "🟢 Low Risk",
            "The stock has shown relatively stable price movements.")
    elif volatility < 35:
        return (
            "🟡 Medium Risk",
            "The stock has moderate price fluctuations.")
    else:
        return (
            "🔴 High Risk",
            "The stock has experienced large price swings and may be more suitable for investors with a higher risk tolerance.")
def calculate_score(data, volatility):
#calculating teh investment score out of 100

    score = 0
    reasons=[]

    current_price = data["Close"].iloc[-1]

    ma20 = data["MA20"].iloc[-1]
    ma50 = data["MA50"].iloc[-1]
    ma200 = data["MA200"].iloc[-1]
    if pd.isna(ma20) or pd.isna(ma50) or pd.isna(ma200):
     return 0, ["Not enough historical data"], 0
    current_macd = data["MACD"].iloc[-1]
    current_signal = data["Signal"].iloc[-1]
    yearly_return = (
        (current_price - data["Close"].iloc[0])
        / data["Close"].iloc[0]
    ) * 100


    # Rule 1
    if current_price > ma20:# suppose the average is 102 and todays prices is 106 sothe stock is trading above its recent average.
        score += 10#this suggets short term bullish
        reasons.append("Price is above the 20-Day Moving Average this means the Short-term trend is positive")
        #this means Buyers have recently been willing to pay more than the average price over the last month.
    # Rule 2
    if current_price > ma50:#MA50 represents roughly 2–3 months of trading.and if it is above the ma50 thenthe stock is performing good for the medium period
    #this is more strong than ma20
        score += 15
        reasons.append("Price is above the 50-Day Moving Average (Medium-term trend is positive).")
    # Rule 3
    if current_price > ma200:#if the cp is > ma200 then many interpret this as The stock is in a long-term uptrend
        score += 20
        reasons.append("Price is above the 200-Day Moving Average (Long-term trend is positive).")
    # Rule 4     if an year ago the price was 100 and today it is 120 tehn That means the company has created value over the last year.
    #Financially, this tells usthat The stock has rewarded investors over the past year. Momentum has generally been positive
    if yearly_return > 0:
        score += 10
   # Rule 5
    if ma20 > ma50:
        score += 10
        reasons.append("20-Day MA is above the 50-Day MA (Momentum is strengthening).")
    # Rule 6
    if ma50 > ma200:
        score += 15
        reasons.append("50-Day MA is above the 200-Day MA (Long-term trend is healthy).")
    # Rule 7
    if yearly_return > 0:
        score += 10
        reasons.append(f"Positive one-year return ({yearly_return:.2f}%).")
    # Rule 8 this tells us the risk and not the return ;For many long-term investors, lower volatility is desirable because returns are more predictable
    if volatility < 20:
        score += 20
        reasons.append("Low volatility (Lower investment risk).")
    elif volatility < 35:
        score += 10
        reasons.append("Moderate volatility (Moderate investment risk).")
    return score,reasons,yearly_return
def generate_recommendation(score):
    if score >= 85:
        return (
            "🟢 STRONG BUY",
            "The stock has strong technical indicators and positive news sentiment."
        )
    elif score >= 70:
        return (
            "🟢 BUY",
            "The stock has good technical strength and moderate investment risk."
        )
    elif score >= 50:
        return (
            "🟡 HOLD",
            "The stock shows mixed signals. Waiting for confirmation may be appropriate."
        )
    else:
        return (
            "🔴 WAIT AND WATCH",
            "The stock currently shows weak technical indicators or elevated risk."
        )
def final_score(technical_score, news_summary):
 #adjusting the technical score with teh overall score
    score = technical_score
    if news_summary["Overall"] == "Positive":
        score += 5
    elif news_summary["Overall"] == "Negative":#+-5 only beacuse teh small chnages keeps the reccomendation balanced
        score -= 5
    # Keeping the score between 0 and 100
    score = max(0, min(score, 100))
    return score
def trend_analysis(data):
    #thiswill be telling us the overall market trend 
    current_price = data["Close"].iloc[-1]
    ma20 = data["MA20"].iloc[-1]
    ma50 = data["MA50"].iloc[-1]
    ma200 = data["MA200"].iloc[-1]

    if current_price > ma20 > ma50 > ma200:
        trend = "Strong Bullish"
        explanation = (
            "The stock is trading above all major moving averages, "
            "indicating a strong uptrend."
        )
    elif current_price > ma50 > ma200:
        trend = "Bullish"
        explanation = (
            "The stock is trading above its medium and long-term averages."
        )
    elif current_price < ma20 < ma50 < ma200:
        trend = "Strong Bearish"
        explanation = (
            "The stock is trading below all major moving averages."
        )
    elif current_price < ma50 < ma200:
        trend = "Bearish"
        explanation = (
            "The stock is below important moving averages."
        )
    else:
        trend = "Sideways"
        explanation = (
            "The stock is moving within a range without a clear trend."
        )
    return trend, explanation