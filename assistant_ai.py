def answer_question(
    question,
    company,
    recommendation,
    risk,
    confidence,
    fundamentals,
    news_summary,
    levels,
    thesis
):

    question = question.lower()

    if any(word in question for word in [
    "buy",
    "invest",
    "purchase",
    "should i buy",
    "should i invest"
    ]):

        return (
            f"The current recommendation is **{recommendation}**.\n\n"
            f"{thesis}"
        )

    elif any(word in question for word in [
    "risk",
    "safe",
    "danger",
    "volatile"
    ]):

        return (
            f"Current Risk Level: **{risk}**.\n\n"
            "This assessment considers volatility, technical trend, and overall market conditions."
        )

    elif "confidence" in question:

        return (
            f"The confidence score is **{confidence}%**."
        )

    elif any(word in question for word in [
    "fundamental",
    "pe",
    "roe",
    "eps",
    "profit"
    ]):

        return (
            f"""
        PE Ratio : {fundamentals['PE Ratio']}

        ROE : {fundamentals['Return on Equity']}

        Profit Margin : {fundamentals['Profit Margin']}
        """
                )

    elif any(word in question for word in [
    "news",
    "sentiment",
    "headline"
    ]):

        return (
            f"Overall News Sentiment : {news_summary['Overall']}"
        )

    elif any(word in question for word in [
    "support",
    "resistance",
    "target",
    "price"
    ]):

        return (
            f"""
        Support : ₹{levels['Support']}

        Resistance : ₹{levels['Resistance']}
        """
                )

    else:

        return (
            "Based on the available analysis, the stock should be evaluated using the AI thesis, fundamentals, technical indicators, and recent news before making an investment decision."
        )
