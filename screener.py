def generate_ai_insights(
    ticker,
    adjusted_score,
    recommendation,
    risk,
    confidence,
    trend_explanation,
    strengths,
    weaknesses
):
    insights = []

    insights.append(f"🤖 AI Market Insight for {ticker}")
    insights.append("")

    insights.append(
        f"The current quantitative score is {adjusted_score:.2f}, "
        f"with a recommendation of {recommendation}."
    )

    insights.append("")

    insights.append(
        f"Risk assessment: {risk}. "
        f"Model confidence: {confidence}%."
    )

    insights.append("")

    insights.append(f"📈 Trend: {trend_explanation}")

    insights.append("")

    if strengths:
        insights.append("✅ Key strengths:")
        for strength in strengths:
            insights.append(f"• {strength}")

    insights.append("")

    if weaknesses:
        insights.append("⚠️ Key risks:")
        for weakness in weaknesses:
            insights.append(f"• {weakness}")

    insights.append("")
    insights.append(
        "This insight is based on the quantitative analysis performed "
        "by EquityInsights and should not be considered financial advice."
    )

    return insights