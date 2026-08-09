from collections import Counter
#the technical analyst
def technical_member(stock_data, levels):
    reasons = []
    vote = "HOLD"
    price = stock_data["Close"].iloc[-1]
    ma50 = stock_data["MA50"].iloc[-1]
    rsi = stock_data["RSI"].iloc[-1]
    macd = stock_data["MACD"].iloc[-1]
    signal = stock_data["Signal"].iloc[-1]
    score = 0
    # the Moving Average
    if price > ma50:
        score += 1
        reasons.append("Price is trading above MA50.")
    else:
        reasons.append("Price is below MA50.")
    # RSI
    if 40 <= rsi <= 70:
        score += 1
        reasons.append("RSI indicates healthy momentum.")
    elif rsi > 70:
        reasons.append("RSI suggests overbought conditions.")
    else:
        reasons.append("RSI is weak.")
    # MACD
    if macd > signal:
        score += 1
        reasons.append("MACD is above Signal line.")
    else:
        reasons.append("MACD is below Signal line.")
    # Support
    if price > levels["Support"]:
        score += 1
        reasons.append("Price is above support level.")
    if score >= 3:
        vote = "BUY"
    elif score <= 1:
        vote = "SELL"
    return {
        "Member": "📈 Technical Analyst",
        "Vote": vote,
        "Reason": reasons
    }
#the fundamental analyst
def fundamental_member(fundamentals):
    reasons = []
    score = 0
    vote = "HOLD"
    pe = fundamentals.get("PE Ratio", 0)
    roe = fundamentals.get("ROE", 0)
    debt = fundamentals.get("Debt/Equity", 0)
    if roe > 15:
        score += 1
        reasons.append("Strong ROE.")
    else:
        reasons.append("Average ROE.")
    if pe < 30:
        score += 1
        reasons.append("Reasonable valuation.")
    else:
        reasons.append("Valuation appears expensive.")
    if debt < 1:
        score += 1
        reasons.append("Low debt.")
    else:
        reasons.append("Debt is relatively high.")
    if score >= 2:
        vote = "BUY"
    elif score == 1:
        vote = "HOLD"
    else:
        vote = "SELL"
    return {
        "Member": "📊 Fundamental Analyst",
        "Vote": vote,
        "Reason": reasons
    }
#news analyst
def news_member(news_summary):
    overall = news_summary["Overall"]
    if overall == "Positive":
        vote = "BUY"
        reasons = [
            "Overall news sentiment is positive."
        ]
    elif overall == "Negative":
        vote = "SELL"
        reasons = [
            "Overall news sentiment is negative."
        ]
    else:
        vote = "HOLD"
        reasons = [
           "News sentiment is neutral."
        ]
    return {
        "Member": "📰 News Analyst",
        "Vote": vote,
        "Reason": reasons
    }
#risk  analyst
def risk_member(risk):
    if risk == "Low":
        vote = "BUY"
        reasons = [
            "Overall investment risk is low."
        ]
    elif risk == "Medium":
        vote = "HOLD"
        reasons = [
            "Moderate investment risk."
        ]
    else:
        vote = "SELL"
        reasons = [
           "High investment risk."
        ]
    return {
        "Member": "⚠ Risk Manager",
        "Vote": vote,
        "Reason": reasons
    }
#the final commites decision
def committee_decision(
    stock_data,
    fundamentals,
    news_summary,
    levels,
    risk
):
    members = [
        technical_member(
            stock_data,
            levels
        ),
        fundamental_member(
            fundamentals
        ),
        news_member(
            news_summary
        ),
        risk_member(
           risk
        )
    ]
    votes = [
        member["Vote"]
        for member in members
    ]
    counter = Counter(votes)
    final_vote = counter.most_common(1)[0][0]
    confidence = int(
        counter[final_vote]
        / len(votes)
        * 100
    )
    return members, final_vote, confidence