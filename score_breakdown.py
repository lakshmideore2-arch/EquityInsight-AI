def generate_score_breakdown(
    stock_data,
    volatility,
    news_summary
):

    breakdown = []

    score = 0
    current = stock_data["Close"].iloc[-1]
    ma20 = stock_data["MA20"].iloc[-1]
    ma50 = stock_data["MA50"].iloc[-1]
    ma200 = stock_data["MA200"].iloc[-1]
    yearly_return = (
        (current - stock_data["Close"].iloc[0])
        / stock_data["Close"].iloc[0]
    ) * 100
    if current > ma20:
        breakdown.append(("Price above MA20", 10))
        score += 10
    if current > ma50:
        breakdown.append(("Price above MA50", 15))
        score += 15
    if current > ma200:
        breakdown.append(("Price above MA200", 20))
        score += 20
    if yearly_return > 0:
        breakdown.append(("Positive 1-Year Return", 10))
        score += 10
    if ma20 > ma50:
        breakdown.append(("MA20 above MA50", 10))
        score += 10
    if ma50 > ma200:
        breakdown.append(("MA50 above MA200", 15))
        score += 15
    if volatility < 20:
        breakdown.append(("Low Volatility", 20))
        score += 20
    elif volatility < 35:
        breakdown.append(("Moderate Volatility", 10))
        score += 10
    if news_summary["Overall"] == "Positive":
        breakdown.append(("Positive News", 5))
        score += 5
    elif news_summary["Overall"] == "Negative":
        breakdown.append(("Negative News", -5))
        score -= 5
    return breakdown, score