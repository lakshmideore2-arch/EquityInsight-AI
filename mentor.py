def investment_mentor(
    recommendation,
    risk,
    news_summary,
    levels,
    adjusted_score
):
    advice = []
    advice.append("🤖 AI Mentor")
    advice.append("")
    if adjusted_score >= 85:
        advice.append(
            "The stock currently has very strong technical strength."
        )
    elif adjusted_score >= 70:
        advice.append(
            "The stock has healthy technical indicators but should still be monitored."
        )
    else:
        advice.append(
            "The stock still has uncertainties."
        )
    advice.append("")
    if "Low" in risk:
        advice.append(
            "Risk is relatively low."
        )
    elif "Medium" in risk:
        advice.append(
            "Risk is moderate. Position sizing is important."
        )
    else:
        advice.append(
            "Risk is high. Avoid investing all your capital at once."
        )
    advice.append("")
    if news_summary["Overall"] == "Positive":
        advice.append(
            "Recent news is supporting the current trend."
        )
    elif news_summary["Overall"] == "Negative":
        advice.append(
            "Be cautious because recent news may increase volatility."
        )
    advice.append("")
    advice.append(
        f"Support Level : ₹{levels['Support']}"
    )
    advice.append(
        f"Resistance Level : ₹{levels['Resistance']}"
    )
    advice.append("")
    advice.append(
        "Long-term investors should focus on company quality rather than short-term price movements."
    )
    return advice