from data import get_stock_data
from indicators import calculate_indicators
from analysis import analyze_technical_signals
def timeframe_analysis(ticker):
    timeframes = {
        "3 Minutes": ("7d", "3m"),
        "5 Minutes": ("7d", "5m"),
        "15 Minutes": ("30d", "15m"),
        "30 Minutes": ("60d", "30m"),
        "1 Hour": ("730d", "1h"),
        "1 Day": ("1y", "1d"),
        "1 Week": ("5y", "1wk"),
        "1 Month": ("max", "1mo")
    }
    results = []
    for name, (period, interval) in timeframes.items():
        data = get_stock_data(
            ticker,
            period=period,
            interval=interval
        )
        if data is None or len(data) < 50:
            continue
        data = calculate_indicators(data)
        analysis = analyze_technical_signals(data)
        results.append({
            "Timeframe": name,
            "Trend": analysis["Trend"],
            "Bullish": analysis["Bullish Signals"],
            "Bearish": analysis["Bearish Signals"]
        })
    return results