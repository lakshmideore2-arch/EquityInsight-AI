def generate_opportunities_and_risks(
    stock_data,
    fundamentals,
    news_summary,
    risk
):

    opportunities = []

    risks = []

    current = stock_data["Close"].iloc[-1]

    ma20 = stock_data["MA20"].iloc[-1]
    ma50 = stock_data["MA50"].iloc[-1]
    ma200 = stock_data["MA200"].iloc[-1]

    rsi = stock_data["RSI"].iloc[-1]
    if current > ma200:
        opportunities.append(
            "Strong long-term uptrend."
        )

    if current > ma50:
        opportunities.append(
            "Healthy medium-term momentum."
        )

    if news_summary["Overall"] == "Positive":
        opportunities.append(
            "Positive recent news sentiment."
        )

    roe = fundamentals.get("Return on Equity")

    if isinstance(roe, (int, float)):

        if roe > 15:
            opportunities.append(
                "Strong Return on Equity."
            )

    if rsi > 70:
        risks.append(
            "RSI indicates the stock may be overbought."
        )

    if news_summary["Overall"] == "Negative":
        risks.append(
            "Recent news sentiment is negative."
        )

    if "High" in risk:
        risks.append(
            "High historical volatility."
        )

    pe = fundamentals.get("PE Ratio")

    if isinstance(pe, (int, float)):

        if pe > 40:
            risks.append(
                "High valuation compared to many companies."
            )

    if len(opportunities) == 0:
        opportunities.append(
            "No major opportunity detected currently."
        )

    if len(risks) == 0:
        risks.append(
            "No significant warning signs detected."
        )

    return opportunities, risks