import streamlit as st
from charts import plot_dashboard
from report import display_report
from dashboard import technical_dashboard
from pdf_report import create_pdf
from explainability import explain_decision
from checklist import investment_checklist
from mentor import investment_mentor
from scenario import simulate_scenario
from assistant_ai import answer_question
from gauge import score_gauge
from news_chart import sentiment_chart
from financials import get_financial_statements
from committee import committee_decision
from screener import generate_ai_insights
# Import Project Functions
from monte_carlo import (
    monte_carlo_simulation,
    plot_monte_carlo,
    monte_carlo_statistics
)
from data import (
    get_stock_data,
    get_company_info,
    get_fundamentals,
    get_financial_statements
    
)

from indicators import (
    calculate_indicators,
    calculate_volatility
)

from scoring import (
    calculate_score,
    risk_level,
    final_score,
    generate_recommendation,
    trend_analysis
)

from sentiment import (
    analyze_news_sentiment,
    overall_news_sentiment,
    get_stock_news
)
from watchlist import (
    get_watchlist,
    get_top_gainers,
    get_top_losers
)
from portfolio import (
    generate_portfolio,
    portfolio_chart
)

from report import display_report
from patterns import detect_patterns

from analysis import analyze_technical_signals
from support_resistance import calculate_support_resistance

from market import get_market_overview
from timeframes import get_timeframe_settings
from confidence import calculate_confidence
from pros_cons import generate_pros_cons
from comparison import (compare_stocks,
                        comparison_chart,
                        ai_compare_verdict)
from thesis import generate_investment_thesis
from portfolio import generate_portfolio
from patterns import detect_patterns

from screener import *

from alerts import generate_alerts

def show_analysis():
    if "committee_members" not in st.session_state:
        st.session_state["committee_members"] = None

    if "committee_vote" not in st.session_state:
        st.session_state["committee_vote"] = None

    if "committee_confidence" not in st.session_state:
        st.session_state["committee_confidence"] = None
    st.title("📈 Stock Analysis")
    ticker = st.text_input(
    "Enter Stock Ticker",
    value="AAPL"
        )
    timeframe = st.selectbox(
        "Select Timeframe",
        [
            "1 Minute",
            "3 Minutes",
            "5 Minutes",
            "15 Minutes",
            "30 Minutes",
            "1 Hour",
            "1 Day",
            "1 Week",
            "1 Month"
        ]
    )
    analyze = st.button("Analyze")
    if analyze:
        with st.spinner("Analyzing stock... Please wait..."):

            
                # =====================================
                # Download Stock Data
                # =====================================

                ticker = ticker.strip().upper()

                if ticker == "":
                    st.error("Please enter a stock ticker.")
                    st.stop()   #removing extra space

                period, interval = get_timeframe_settings(timeframe)

                stock_data = get_stock_data(
                    ticker,
                    period=period,
                    interval=interval
                )

                if stock_data is None:
                    st.error("Unable to fetch stock data.")
                    return

                if stock_data.empty:
                    st.error("No stock data available.")
                    return


    #the information of teh company
                company = get_company_info(ticker)
                fundamentals = get_fundamentals(ticker)
                income,balance,cashflow=get_financial_statements(ticker)
            #teh indicators
                stock_data = calculate_indicators(stock_data)
                simulated_prices, mu, sigma = monte_carlo_simulation(stock_data)

                monte_carlo_stats = monte_carlo_statistics(
                    simulated_prices,
                    stock_data["Close"].iloc[-1]
                )
                print("After indicators:")
                print(stock_data[["Close", "MA20", "MA50"]].tail())
                volatility = calculate_volatility(stock_data)
                analysis = analyze_technical_signals(stock_data)
                patterns = detect_patterns(stock_data)
                levels = calculate_support_resistance(stock_data)
                alerts = generate_alerts(stock_data,levels)
                #technical socres
                technical_score, reasons, yearly_return = calculate_score(
                    stock_data,
                    volatility
                )
                trend, trend_explanation = trend_analysis(stock_data)
    #news
                news = get_stock_news(company)
                if not news:
                    st.warning("No recent news found for this company.")

                sentiment_results = analyze_news_sentiment(news)

                news_summary = overall_news_sentiment(
                    sentiment_results
                )
                strengths, weaknesses = generate_pros_cons(stock_data,volatility,news_summary,levels)
    #news
                # =====================================
                # Final Score
                # =====================================

                adjusted_score = final_score(
                    technical_score,
                    news_summary
                )

                # =====================================
                # Recommendation
                # =====================================

                recommendation, explanation = generate_recommendation(
                adjusted_score
                )

                # =====================================
                # Risk
                # =====================================

                risk, risk_explanation = risk_level(volatility)
                confidence=calculate_confidence(adjusted_score,news_summary,volatility)
                # =====================================
                # Report
                # =====================================
                print("Risk variable:", risk)
                print("Type of risk:", type(risk))

                print("Recommendation:", recommendation)
                print("Adjusted Score:", adjusted_score)
                thesis = generate_investment_thesis(
                    company,
                    stock_data,
                    recommendation,
                    risk,
                    news_summary,
                    fundamentals
                )
                members, final_vote, committee_confidence = committee_decision(
                    stock_data,
                    fundamentals,
                    news_summary,
                    levels,
                    risk
                )
                
                
                patterns = detect_patterns(stock_data)
                st.session_state["analysis_done"] = True

                st.session_state["company"] = company
                st.session_state["ticker"] = ticker
                st.session_state["stock_data"] = stock_data
                st.session_state["adjusted_score"] = adjusted_score
                st.session_state["recommendation"] = recommendation
                st.session_state["explanation"] = explanation
                st.session_state["risk"] = risk
                st.session_state["confidence"] = confidence
                st.session_state["reasons"] = reasons
                st.session_state["news_summary"] = news_summary
                st.session_state["news"] = news
                st.session_state["levels"] = levels
                st.session_state["alerts"] = alerts
                st.session_state["patterns"] = patterns
                st.session_state["trend_explanation"] = trend_explanation
                st.session_state["fundamentals"] = fundamentals
                st.session_state["thesis"] = thesis
                st.session_state["strengths"] = strengths
                st.session_state["weaknesses"] = weaknesses
                st.session_state["analysis"] = analysis
                st.session_state["committee_decision"] = members

                st.session_state["final_vote"] = final_vote

                st.session_state["committee_confidence"] = committee_confidence
                st.session_state["simulated_prices"] = simulated_prices
                st.session_state["monte_carlo_stats"] = monte_carlo_stats
                st.divider()
                            
                st.subheader(f"🏢 {company['Name']} ({ticker})")

                st.caption(
                    f"{company['Sector']} | {company['Country']} | {company['Currency']}"
                )

                st.divider()

                top1, top2, top3, top4 = st.columns(4)

                with top1:
                    st.metric(
                        "💲 Current Price",
                        company["Current Price"]
                    )

                with top2:
                    st.metric(
                        "📊 Market Cap",
                        company["Market Cap"]
                    )

                with top3:
                    st.metric(
                        "📈 PE Ratio",
                        company["PE Ratio"]
                    )

                with top4:
                    st.metric(
                        "⚖️ Beta",
                        company["Beta"]
                    )

                st.divider()

                bottom1, bottom2, bottom3 = st.columns(3)

                with bottom1:
                    st.metric(
                        "Recommendation",
                        recommendation
                    )

                with bottom2:
                    st.metric(
                        "Risk",
                        risk
                    )

                with bottom3:
                    st.metric(
                        "Confidence",
                        f"{confidence}%"
                    )
                                
                st.divider()


                st.subheader(f"🏢 {company['Name']} ({ticker})")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "🏭 Sector",
                        company["Sector"]
                    )

                with col2:
                    st.metric(
                        "🌍 Country",
                        company["Country"]
                    )

                with col3:
                    st.metric(
                        "💰 Currency",
                        company["Currency"]
                    )

                st.write(f"**Industry:** {company['Industry']}")

                st.info(
                    f"""
                ### 🤖 AI Recommendation

                {explanation}
                """
                )

                st.divider()
               
                if st.session_state.get("analysis_done", False):
                    st.success("Analysis Completed Successfully!")
                    
        
    #main appplication
    if not st.session_state.get("analysis_done", False):
        st.info("Enter a ticker and click Analyze.")
        return
    company = st.session_state["company"]
    ticker = st.session_state["ticker"]
    stock_data = st.session_state["stock_data"]
    adjusted_score = st.session_state["adjusted_score"]
    recommendation = st.session_state["recommendation"]
    explanation = st.session_state["explanation"]
    risk = st.session_state["risk"]
    confidence = st.session_state["confidence"]
    reasons = st.session_state["reasons"]
    news_summary = st.session_state["news_summary"]
    news = st.session_state["news"]
    levels = st.session_state["levels"]
    alerts = st.session_state["alerts"]
    patterns = st.session_state["patterns"]
    trend_explanation = st.session_state["trend_explanation"]
    fundamentals = st.session_state["fundamentals"]
    thesis = st.session_state["thesis"]
    strengths = st.session_state["strengths"]
    weaknesses = st.session_state["weaknesses"]
    analysis = st.session_state["analysis"]


    tab1, tab2, tab3,tab4 , tab5 = st.tabs(
        [
            "Analysis",
            "AI Insights",
            "Charts",
            "Financial Statements",
            "Monte Carlo"
        ]
    )

    # We'll move all the code here step by step.
    with tab1:

        display_report(
        company,
        ticker,
        stock_data,
        adjusted_score,
        recommendation,
        explanation,
        risk,
        confidence,
        reasons,
        news_summary,
        news,
        levels,
        alerts,
        patterns,
        trend_explanation,
        fundamentals,
        thesis,
        strengths,
        weaknesses
    )   
        st.divider()

        fig = score_gauge(adjusted_score)

        st.plotly_chart(
            fig,
            use_container_width=True
        )
        st.divider()

        st.subheader("📄 Export Investment Report")

        if st.button("Generate PDF Report"):

            filename = f"{ticker}_Investment_Report.pdf"
            technical_summary = [

                    trend_explanation,

                    f"Support Level : ₹{levels['Support']}",

                    f"Resistance Level : ₹{levels['Resistance']}",

                    f"Chart Pattern : {patterns if patterns else 'None'}"

                ]
            members, final_vote, committee_confidence = committee_decision(
                                stock_data,
                                fundamentals,
                                news_summary,
                                levels,
                                risk
                            )
            scenario_name = scenario if 'scenario' in locals() else "Not Run"

            scenario_result = result if 'result' in locals() else ["Scenario not executed."]
            members = st.session_state["committee_decision"]

            committee_confidence = st.session_state["committee_confidence"]

            simulated_prices = st.session_state["simulated_prices"]

            monte_carlo_stats = st.session_state["monte_carlo_stats"]
            create_pdf(
                filename=filename,
                company=company,
                ticker=ticker,
                recommendation=recommendation,
                adjusted_score=adjusted_score,
                confidence=confidence,
                risk=risk,
                thesis=thesis,
                fundamentals=fundamentals,
                reasons=reasons,
                strengths=strengths,
                weaknesses=weaknesses,
                news_summary=news_summary,
                committee_members=members,
                final_vote=final_vote,
                committee_confidence=committee_confidence,
                simulated_prices=simulated_prices,
                monte_carlo_stats=monte_carlo_stats,
                scenario_name=scenario_name,
                scenario_result=scenario_result,
                technical_summary=technical_summary
            )

            with open(filename, "rb") as pdf_file:

                st.download_button(
                    label="⬇ Download PDF Report",
                    data=pdf_file,
                    file_name=filename,
                    mime="application/pdf"
                )

            st.success("PDF Report Generated Successfully!")
    with tab2:

        technical_dashboard(analysis)
        patterns = detect_patterns(stock_data)

        st.subheader("🕯️ Candlestick Pattern Detection")

        if patterns:
            for pattern, explanation in patterns:
                st.success(pattern)
                st.write(explanation)
        else:
            st.info("No significant candlestick patterns detected.")
        st.divider()

        st.subheader("🧠 AI Investment Thesis")
        st.info(thesis)

        st.divider()
        

        st.subheader("🤖 AI Investment Committee")

        committee = st.session_state.get("committee_decision", [])

        if committee:
            for member in committee:
                st.markdown(f"### {member['Member']}")
                st.write(f"**Vote:** {member['Vote']}")

                for reason in member["Reason"]:
                    st.write(f"• {reason}")

            st.success(
                f"""
        ### Final Committee Decision

        **Decision:** {st.session_state['final_vote']}

        **Confidence:** {st.session_state['committee_confidence']}%
        """
            )
        else:
            st.info("Run an analysis to generate the committee decision.")

        if st.session_state.get("chat_response"):

            st.success(st.session_state.chat_response)

            st.header("✅ AI Investment Checklist")

            items = investment_checklist(
                stock_data,
                recommendation,
                risk,
                news_summary,
                fundamentals,
                levels
            )

            for item in items:
                st.write(item)

            st.divider()

        st.header("🎓 AI Investment Mentor")

        mentor = investment_mentor(
            recommendation,
            risk,
            news_summary,
            levels,
            adjusted_score
        )

        for line in mentor:
            st.write(line)
        st.divider()
        st.divider()

        st.header("💬 Ask EquityInsight AI")

        question = st.text_input(
            "Ask anything about this stock...",
            placeholder="Example: Should I buy this stock?"
        )

        if st.button("Ask AI"):

            if question.strip() == "":

                st.warning("Please enter a question.")

            else:

                answer = answer_question(

                    question,

                    company,

                    recommendation,

                    risk,

                    confidence,

                    fundamentals,

                    news_summary,

                    levels,

                    thesis

                )

                st.success(answer)

        st.header("🧠 AI Scenario Simulator")

        scenario = st.selectbox(
            "Choose a scenario",
            [
                "Stock falls 10%",
                "Positive Earnings",
                "Negative Earnings",
                "Interest Rate Hike",
                "Interest Rate Cut"
            ],
            key="scenario_box"
        )

        if st.button("Run Scenario", key="scenario_button"):

            result = simulate_scenario(
                scenario,
                recommendation,
                risk,
                news_summary,
                adjusted_score,
                levels
            )
            st.markdown("\n\n".join(result))
        
        st.subheader("🤖 AI Insights")
        confidence=st.session_state["confidence"]
        insights = generate_ai_insights(
            ticker=ticker,
            adjusted_score=adjusted_score,
            recommendation=recommendation,
            risk=risk,
            confidence=confidence,
            trend_explanation=trend_explanation,
            strengths=strengths,
            weaknesses=weaknesses
        )

        for insight in insights:
            st.write(insight)
        
                    
    with tab3:

        fig = plot_dashboard(
            stock_data,
            company["Name"]
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with tab4:
        financials, balance_sheet, cash_flow = get_financial_statements(ticker)

        st.subheader("📄 Income Statement")

        if not financials.empty:
            st.dataframe(financials)
        else:
            st.info("Income Statement not available.")

        st.divider()

        st.subheader("🏦 Balance Sheet")

        if not balance_sheet.empty:
            st.dataframe(balance_sheet)
        else:
            st.info("Balance Sheet not available.")

        st.divider()

        st.subheader("💰 Cash Flow Statement")

        if not cash_flow.empty:
            st.dataframe(cash_flow)
        else:
            st.info("Cash Flow Statement not available.")
    with tab5:

        st.subheader("🎲 Monte Carlo Price Simulation")

        simulated_prices, mu, sigma = monte_carlo_simulation(
            stock_data
        )

        fig = plot_monte_carlo(simulated_prices)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        stats = monte_carlo_statistics(
            simulated_prices,
            stock_data["Close"].iloc[-1]
        )
        st.divider()

        st.subheader("Monte Carlo Risk Analytics")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Expected Price",
                f"₹{stats['Expected Price']:.2f}"
            )

        with col2:
            st.metric(
                "Probability of Profit",
                f"{stats['Probability of Profit']:.1f}%"
            )

        with col3:
            st.metric(
                "95% Confidence Range",
                f"₹{stats['Lower CI']:.2f} - ₹{stats['Upper CI']:.2f}"
            )

        st.divider()

        col4, col5 = st.columns(2)

        with col4:
            st.metric(
                "📈 Best Case",
                f"₹{stats['Best Case']:.2f}"
            )

        with col5:
            st.metric(
                "📉 Worst Case",
                f"₹{stats['Worst Case']:.2f}"
            )
