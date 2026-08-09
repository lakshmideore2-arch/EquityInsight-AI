def generate_pros_cons(stock_data,volatility,news_summary,levels):
    strengths = []
    weaknesses = []
    current = stock_data["Close"].iloc[-1]
    ma20 = stock_data["MA20"].iloc[-1]
    ma50 = stock_data["MA50"].iloc[-1]
    ma200 = stock_data["MA200"].iloc[-1]
    rsi = stock_data["RSI"].iloc[-1]
    macd = stock_data["MACD"].iloc[-1]
    signal = stock_data["Signal"].iloc[-1]
    if current > ma200:
        strengths.append(
            "Price is trading above the 200-Day Moving Average (strong long-term trend)."
        )
    else:
        weaknesses.append(
            "Price is below the 200-Day Moving Average."
        )
    if current > ma50:
        strengths.append(
            "Price is above the 50-Day Moving Average."
        )
    else:
        weaknesses.append(
            "Price is below the 50-Day Moving Average."
        )
    if rsi < 30:
        strengths.append(
            "RSI indicates the stock may be oversold."
        )
    elif rsi > 70:
        weaknesses.append(
            "RSI suggests the stock is overbought."
        )
    else:
        strengths.append(
            "RSI is in a healthy range."
        )
    if macd > signal:
        strengths.append(
            "MACD is above the Signal Line (bullish momentum)."
        )
    else:
        weaknesses.append(
            "MACD is below the Signal Line."
        )
    if volatility < 20:
        strengths.append(
            "Low volatility indicates relatively stable price movement."
        )
    elif volatility > 40:
        weaknesses.append(
            "High volatility increases investment risk."
        )
    if news_summary["Overall"] == "Positive":
        strengths.append(
            "Recent news sentiment is positive."
        )
    elif news_summary["Overall"] == "Negative":
        weaknesses.append(
            "Recent news sentiment is negative."
        )
    if levels["Upside"] > 10:
        strengths.append(
            "The stock has good upside potential."
        )
    else:
        weaknesses.append(
            "Limited upside before resistance."
        )
    return strengths, weaknesses