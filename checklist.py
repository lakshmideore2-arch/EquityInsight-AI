def investment_checklist(
    stock_data,
    recommendation,
    risk,
    news_summary,
    fundamentals,
    levels
):
    checklist = []
    current = stock_data["Close"].iloc[-1]
    ma20 = stock_data["MA20"].iloc[-1]
    ma50 = stock_data["MA50"].iloc[-1]
    if current > ma20:
        checklist.append("✅ Price is above 20-Day Moving Average")
    else:
        checklist.append("❌ Price is below 20-Day Moving Average")
    if current > ma50:
        checklist.append("✅ Medium-term trend is positive")
    else:
        checklist.append("❌ Medium-term trend is weak")
    if news_summary["Overall"] == "Positive":
        checklist.append("✅ Recent news sentiment is positive")
    elif news_summary["Overall"] == "Neutral":
        checklist.append("🟡 News sentiment is neutral")
    else:
        checklist.append("❌ Recent news sentiment is negative")
    if "Low" in risk:
        checklist.append("✅ Low investment risk")
    elif "Medium" in risk:
        checklist.append("🟡 Moderate investment risk")
    else:
        checklist.append("❌ High investment risk")
    if fundamentals["Return on Equity"] != "N/A":
        checklist.append(
            f"✅ Return on Equity: {fundamentals['Return on Equity']}"
        )
    if recommendation == "🟢 STRONG BUY":
        checklist.append(
            "🚀 Technical indicators strongly support buying."
        )
    checklist.append(
        f"📍 Consider accumulating near support at ₹{levels['Support']}"
    )
    return checklist