import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from gnews import GNews
from data import get_company_info
from transformers import pipeline
import streamlit as st 

@st.cache_resource(show_spinner=False)
def get_sentiment_analyzer():
    with st.spinner("Getting the news sentiments"):
        return pipeline(
            "sentiment-analysis",
            model="ProsusAI/finbert"
        )
@st.cache_data(ttl=300,show_spinner=False)
def get_stock_news(company, max_news=7):
    with st.spinner("Getting the stock news"):
#eftching the latest financial data
        google_news = GNews(
            language="en",
            country="IN",
            period="7d"
        )
        company_name = company["Name"]
        search_query = (
            f"{company_name} "
            f"{company['Country']} "
            "stock finance"
        )
        news=google_news.get_news(search_query)
        return news[:max_news]
@st.cache_data(ttl=300,show_spinner=False)
def analyze_news_sentiment(news):
    with st.spinner("ananlysing the news sentiments"):
#analysing the data using finbert
        sentiment_results = []
        sentiment_analyzer = get_sentiment_analyzer()
        for article in news:
            title = article["title"]
            result = sentiment_analyzer(title)[0]
            sentiment_results.append({
                "Headline": title,
                "Sentiment": result["label"].capitalize(),
                "Confidence": result["score"]
            })
        return sentiment_results
#getting teh overall news sentimenst 
@st.cache_data(ttl=300,show_spinner=False)
def overall_news_sentiment(sentiment_results):
    with st.spinner("Overall news sentiments"):
        """
        Calculates overall news sentiment.
        """
        positive = 0
        neutral = 0
        negative = 0
        for item in sentiment_results:
            if item["Sentiment"] == "Positive":
                positive += 1
            elif item["Sentiment"] == "Neutral":
                neutral += 1
            else:
                negative += 1
        if positive > negative:
            overall = "Positive"
        elif negative > positive:
            overall = "Negative"
        else:
            overall = "Neutral"
        return {
            "Positive": positive,
            "Neutral": neutral,
            "Negative": negative,
            "Overall": overall
        }