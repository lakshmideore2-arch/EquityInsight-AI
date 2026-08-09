def calculate_confidence(score,news_summary,volatility):
    confidence=score
    if news_summary["Overall"]=="Positive":
        confidence+=5
    elif  news_summary["Overall"]=="Negative":
        confidence -=5

    if volatility<20:
        confidence+=5
    elif    volatility>40:
        confidence-=5

    confidence=max(0,min(100,confidence))
    return round(confidence)
