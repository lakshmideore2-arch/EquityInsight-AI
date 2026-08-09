import plotly.express as px
import pandas as pd
def sentiment_chart(news_summary):
    data = pd.DataFrame({
        "Sentiment": [
            "Positive",
            "Neutral",
            "Negative"
        ],
        "Articles": [
            news_summary["Positive"],
            news_summary["Neutral"],
            news_summary["Negative"]
        ]
    })
    fig = px.pie(
        data,
        names="Sentiment",
        values="Articles",
        title="📰 News Sentiment Distribution"
    )
    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )
    fig.update_layout(
        template="plotly_white"
    )
    return fig