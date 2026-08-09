def generate_alerts(stock_data, levels):
    alerts = []
    current = stock_data["Close"].iloc[-1]
    support = levels["Support"]
    resistance = levels["Resistance"]
    rsi = stock_data["RSI"].iloc[-1]
    # Support Alert
    if current <= support * 1.02:
        alerts.append(
            "🟢 Price is approaching a support level. Buying interest may increase."
        )
    # Resistance Alert
    if current >= resistance * 0.98:
        alerts.append(
            "🔴 Price is approaching resistance. Profit booking may occur."
        )
    # RSI
    if rsi > 70:
        alerts.append(
            "🔴 RSI indicates the stock is overbought."
        )
    elif rsi < 30:
        alerts.append(
            "🟢 RSI indicates the stock is oversold."
        )
    if not alerts:
        alerts.append(
            "✅ No important technical alerts today."
        )
    if stock_data["MACD"].iloc[-1] > stock_data["Signal"].iloc[-1]:
        alerts.append(
            "🟢 MACD has crossed above the Signal Line. Bullish momentum is strengthening."
        )
    if stock_data["MA20"].iloc[-1] > stock_data["MA50"].iloc[-1]:
        alerts.append(
            "🟢 Short-term trend remains stronger than the medium-term trend."
        )
    return alerts