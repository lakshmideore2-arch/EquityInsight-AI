def explain_decision(
    score,
    recommendation,
    reasons,
    news_summary,
    risk
):
    explanation = []
    explanation.append(
        f"Final Score : {score}/100"
    )
    explanation.append(
        f"Recommendation : {recommendation}"
    )
    explanation.append(
        f"Risk Level : {risk}"
    )
    explanation.append("")
    explanation.append("Decision Factors")
    for reason in reasons:
        explanation.append(f"✔ {reason}")
    explanation.append("")
    explanation.append(
        f"Overall News Sentiment : {news_summary['Overall']}"
    )
    return explanation