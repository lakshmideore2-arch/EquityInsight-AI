from reportlab.platypus import (#page layout and typography using scripts
    SimpleDocTemplate,#pdf file 
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import darkblue

def create_pdf(
    filename,
    company,
    ticker,
    recommendation,
    adjusted_score,
    confidence,
    risk,
    thesis,
    fundamentals,
    reasons,
    strengths,
    weaknesses,
    news_summary,
    committee_members,
    final_vote,
    committee_confidence,
    simulated_prices,
    monte_carlo_stats,
    scenario_name,
    scenario_result,
    technical_summary
):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    title_style.alignment = TA_CENTER
    title_style.textColor = darkblue
    heading = styles["Heading2"]
    normal = styles["BodyText"]
    story = []
    # Title

# Cover Page

    from datetime import datetime
    story.append(
        Paragraph(
            "EquityInsight AI",
            title_style
        )
    )
    story.append(Spacer(1,10))
    story.append(
        Paragraph(
            "<b>Professional Investment Research Report</b>",
            heading
        )
    )
    story.append(Spacer(1,20))
    story.append(
        Paragraph(
            f"<b>Company :</b> {company['Name']}",
            normal
        )
    )
    story.append(
        Paragraph(
            f"<b>Ticker :</b> {ticker}",
            normal
        )
    )
    story.append(
        Paragraph(
            f"<b>Generated :</b> {datetime.now().strftime('%d %B %Y  %H:%M')}",
            normal
        )
    )
    story.append(Spacer(1,30))
    # Executive Summary
    story.append(
        Paragraph(
            "Executive Summary",
            heading
        )
    )
    story.append(
        Paragraph(
            f"<b>Recommendation :</b> {recommendation}",
            normal
        )
    )
    story.append(
        Paragraph(
            f"<b>AI Score :</b> {adjusted_score}/100",
            normal
        )
    )
    story.append(
        Paragraph(
            f"<b>Confidence :</b> {confidence}%",
            normal
        )
    )
    story.append(
        Paragraph(
            f"<b>Risk Level :</b> {risk}",
            normal
        )
    )
    story.append(
        Paragraph(
            f"<b>Committee Decision :</b> {final_vote}",
            normal
        )
    )
    story.append(
        Paragraph(
            f"<b>Committee Agreement :</b> {committee_confidence}%",
            normal
        )
    )
    story.append(Spacer(1,25))
    # Company Profile
    story.append(
        Paragraph(
            "Company Profile",
            heading
        )
    )
    story.append(
        Paragraph(
            f"<b>Company Name :</b> {company['Name']}",
            normal
        )
    )
    story.append(
        Paragraph(
            f"<b>Ticker :</b> {ticker}",
            normal
        )
    )
    story.append(
        Paragraph(
            f"<b>Sector :</b> {company['Sector']}",
            normal
        )
    )
    story.append(
        Paragraph(
            f"<b>Industry :</b> {company.get('Industry','N/A')}",
            normal
        )
    )
    story.append(
        Paragraph(
            f"<b>Country :</b> {company.get('Country','N/A')}",
            normal
        )
    )
    story.append(
        Paragraph(
            f"<b>Exchange :</b> {company.get('Exchange','N/A')}",
            normal
        )
    )
    story.append(
        Spacer(1,25)
    )
    # Summary
    story.append(
        Paragraph(
            "<b>Investment Summary</b>",
            heading
        )
    )
    story.append(
        Paragraph(
            f"Recommendation : {recommendation}",
            normal
        )
    )
    story.append(
        Paragraph(
            f"Score : {adjusted_score}/100",
            normal
        )
    )
    story.append(
        Paragraph(
            f"Confidence : {confidence}%",
            normal
        )
    )
    story.append(
        Paragraph(
            f"Risk : {risk}",
            normal
        )
    )
    story.append(
        Spacer(1,20)
    )
    # Financial Health
    story.append(
        Paragraph(
            "Financial Health",
            heading
        )
    )
    important_metrics = [
        "Market Cap",
        "PE Ratio",
        "EPS",
        "ROE",
        "Debt/Equity",
        "Dividend Yield"
    ]
    for metric in important_metrics:
        value = fundamentals.get(metric, "N/A")
        story.append(
            Paragraph(
                f"<b>{metric} :</b> {value}",
                normal
            )
        )
    story.append(
        Spacer(1,25)
    )
#technical analysis
    story.append(
        Paragraph(
            "Technical Analysis Summary",
            heading
        )
    )
    for item in technical_summary:
        story.append(
            Paragraph(
                f"• {item}",
                normal
            )
        )
    story.append(Spacer(1,25))
#strengths
    story.append(
        Paragraph(
            "<b>Strengths</b>",
            heading
       )
    )
    for item in strengths:
        story.append(
            Paragraph(
                f"• {item}",
                normal
            )
        )
    story.append(
        Spacer(1,20)
    )
#Weaknesses
    story.append(
        Paragraph(
            "<b>Weaknesses</b>",
            heading
       )
    )
    for item in weaknesses:
        story.append(
            Paragraph(
                f"• {item}",
                normal
            )
        )
    story.append(
        Spacer(1,20)
    )
#the AI investment committee
    story.append(
        Paragraph(
            "AI Investment Committee",
            heading
        )
    )
    for member in committee_members:
        story.append(
            Paragraph(
                f"<b>{member['Member']}</b>",
                heading
            )
        )
        story.append(
            Paragraph(
                f"<b>Vote :</b> {member['Vote']}",
                normal
            )
        )
        story.append(
            Paragraph(
                "<b>Reasons</b>",
                normal
            )
        )
        for reason in member["Reason"]:
            story.append(
                Paragraph(
                    f"• {reason}",
                    normal
                )
            )
        story.append(Spacer(1,12))

    story.append(
        Paragraph(
            "<b>Final Committee Decision</b>",
            heading
        )
    )
    story.append(
        Paragraph(
            f"Recommendation : <b>{final_vote}</b>",
            normal
        )
    )
    story.append(
        Paragraph(
            f"Committee Agreement : <b>{committee_confidence}%</b>",
            normal
        )
    )
    story.append(Spacer(1,25))
#news
    story.append(
        Paragraph(
            "<b>News Sentiment</b>",
            heading
        )
    )
    story.append(
        Paragraph(
            f"Positive : {news_summary['Positive']}",
            normal
        )
    )
    story.append(
        Paragraph(
            f"Neutral : {news_summary['Neutral']}",
            normal
        )
    )
    story.append(
        Paragraph(
            f"Negative : {news_summary['Negative']}",
            normal
        )
    )
    story.append(
        Paragraph(
            f"Overall : {news_summary['Overall']}",
            normal
        )
    )
    story.append(
        Spacer(1,20)
    )
# Monte Carlo Risk Analysis
    story.append(
        Paragraph(
            "Monte Carlo Risk Analysis",
            heading
        )
    )
    story.append(
        Paragraph(
            f"<b>Expected Price :</b> ₹{monte_carlo_stats['Expected Price']:.2f}",
            normal
        )
    )
    story.append(
        Paragraph(
            f"<b>Probability of Profit :</b> {monte_carlo_stats['Probability of Profit']:.1f}%",
            normal
        )
    )
    story.append(
        Paragraph(
            f"<b>Best Case :</b> ₹{monte_carlo_stats['Best Case']:.2f}",
            normal
        )
    )
    story.append(
        Paragraph(
            f"<b>Worst Case :</b> ₹{monte_carlo_stats['Worst Case']:.2f}",
            normal
        )
    )
    story.append(
        Paragraph(
            f"<b>95% Confidence Interval :</b> ₹{monte_carlo_stats['Lower CI']:.2f} - ₹{monte_carlo_stats['Upper CI']:.2f}",
            normal
        )
    )
    story.append(Spacer(1,25))
#Disclaimer
    story.append(
        Paragraph(
            "<b>Disclaimer</b>",
            heading
        )
    )
    story.append(
        Paragraph(
            "This report is AI generated and is intended only for educational purposes. It should not be considered financial advice. Always perform your own research before making investment decisions.",
            normal
        )
    )
    doc.build(story)