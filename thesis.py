def generate_investment_thesis(
    company,
    stock_data,
    recommendation,
    risk,
    news_summary,
    fundamentals
):  
#generating the thesis using all the technical indicators
    thesis = []
    current_price = stock_data["Close"].iloc[-1]
    ma20 = stock_data["MA20"].iloc[-1]
    ma50 = stock_data["MA50"].iloc[-1]
    ma200 = stock_data["MA200"].iloc[-1]
    rsi = stock_data["RSI"].iloc[-1]
    if current_price > ma200:
        thesis.append(
            "The stock is trading above its 200-Day Moving Average, indicating a strong long-term upward trend."
        )
    else:
        thesis.append(
            "The stock is currently trading below its 200-Day Moving Average, suggesting long-term weakness."
        )
    if current_price > ma50:
        thesis.append(
            "Price remains above the 50-Day Moving Average, reflecting healthy medium-term momentum."
        )
    else:
        thesis.append(
            "The stock is below its 50-Day Moving Average, showing weaker medium-term momentum."
        )
    if current_price > ma20:
        thesis.append(
            "Recent price action remains positive as the stock trades above its 20-Day Moving Average."
        )
    else:
        thesis.append(
            "Recent trading activity has weakened as the stock remains below its 20-Day Moving Average."
        )
    if rsi > 70:
        thesis.append(
            "The RSI indicates that the stock is currently overbought, which may lead to short-term profit booking."
        )
    elif rsi < 30:
        thesis.append(
            "The RSI suggests the stock is oversold, which sometimes presents buying opportunities."
        )
    else:
        thesis.append(
            "The RSI remains in a healthy neutral range without indicating excessive buying or selling pressure."
        )
    overall = news_summary["Overall"]
    if overall == "Positive":
        thesis.append(
            "Recent news sentiment is positive, which supports investor confidence."
        )
    elif overall == "Negative":
        thesis.append(
            "Recent news sentiment is negative and may increase uncertainty."
        )
    else:
        thesis.append(
            "Recent news flow remains largely neutral."
        )
    if "Low" in risk:
        thesis.append(
            "Historical volatility remains low, suggesting relatively stable price behaviour."
        )
    elif "Medium" in risk:
        thesis.append(
            "Price volatility is moderate, indicating balanced investment risk."
        )
    else:
        thesis.append(
            "Historical volatility is high, making the stock suitable mainly for investors comfortable with larger price swings."
        )
    roe = fundamentals.get("Return on Equity")
    if isinstance(roe, (int, float)):
        if roe > 15:
            thesis.append(
                "The company generates strong returns on shareholder equity, indicating efficient management."
            )
        elif roe > 8:
            thesis.append(
                "Return on Equity is satisfactory but leaves room for improvement."
            )
        else:
            thesis.append(
                "Return on Equity remains relatively weak compared with stronger businesses."
            )
    thesis.append(
        f"Overall, the stock currently receives a **{recommendation}** recommendation based on technical strength, risk profile, company fundamentals, and recent news sentiment."
    )
    return "\n\n".join(thesis)