def explain_portfolio(portfolio_df, risk_preference):
    if portfolio_df.empty:

        return [
            "🤖 AI Portfolio Explanation",
            "",
            "No portfolio has been created yet.",
            "Please add stocks and generate a portfolio first."
        ]

    explanation = []

    explanation.append("🤖 AI Portfolio Explanation")
    explanation.append("")

    explanation.append(
        f"This portfolio has been constructed for a **{risk_preference}** risk investor."
    )

    largest = portfolio_df.iloc[0]

    explanation.append(
        f"The largest allocation has been assigned to **{largest['Ticker']}**, as it achieved the highest overall investment score among the selected companies."
    )

    explanation.append("")

    if risk_preference == "Low":
        explanation.append(
            "The portfolio emphasizes capital preservation by allocating more weight to relatively stable investments with lower expected volatility."
        )

    elif risk_preference == "Medium":
        explanation.append(
            "The portfolio seeks a balance between long-term growth and investment stability, providing moderate exposure to risk."
        )

    else:
        explanation.append(
            "The portfolio is designed for long-term capital appreciation and therefore accepts higher market volatility in pursuit of stronger returns."
        )

    explanation.append("")

    explanation.append(
        "The allocation has also been diversified across multiple companies to reduce concentration risk and improve overall portfolio resilience."
    )

    explanation.append("")

    explanation.append(
        "Although this portfolio is generated using quantitative analysis and AI-assisted scoring, investment decisions should always be supported by independent research and periodic portfolio review."
    )

    return explanation
