def get_timeframe_settings(timeframe):
    mapping = {
    "1 Minute": ("7d", "1m"),
    "3 Minutes": ("30d", "2m"),
    "5 Minutes": ("60d", "5m"),
    "15 Minutes": ("60d", "15m"),
    "30 Minutes": ("60d", "30m"),
    "1 Hour": ("730d", "60m"),
    "1 Day": ("5y", "1d"),
    "1 Week": ("10y", "1wk"),
    "1 Month": ("max", "1mo"),
    }
    return mapping[timeframe]