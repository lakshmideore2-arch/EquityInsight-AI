def simulate_scenario(
    scenario,
    recommendation,
    risk,
    news_summary,
    adjusted_score,
    levels
):
    result = []
    if scenario == "Stock falls 10%":
        result.append("📉 Scenario: Stock falls by 10%")
        result.append("")
        if adjusted_score >= 70:
            result.append(
                "The overall technical trend is still strong."
            )
            result.append(
                "The correction may provide a buying opportunity."
            )

        else:
            result.append(
                "A further decline could weaken the existing trend."
            )
        result.append(
            f"Watch Support Level around ₹{levels['Support']}"
        )

    elif scenario == "Positive Earnings":
        result.append("📈 Scenario: Company beats earnings")
        result.append("")
        result.append(
            "Positive earnings generally improve investor confidence."
        )
        result.append(
            "Buying pressure may increase."
        )
        if news_summary["Overall"] == "Positive":
            result.append(
                "Positive news sentiment further strengthens this scenario."
            )

    elif scenario == "Negative Earnings":
        result.append("📉 Scenario: Company misses earnings")
        result.append("")
        result.append(
            "Selling pressure may increase."
        )
        result.append(
            "Support levels should be monitored closely."
        )
    elif scenario == "Interest Rate Hike":
        result.append("🏦 Scenario: Interest rates increase")
        result.append("")
        result.append(
            "Higher interest rates often reduce market liquidity."
        )
        result.append(
            "Growth stocks may experience additional pressure."
        )
    elif scenario == "Interest Rate Cut":
        result.append("💰 Scenario: Interest rates decrease")
        result.append("")
        result.append(
            "Lower rates generally support equity markets."
        )
        result.append(
            "Investor sentiment may improve."
        )
    result.append("")
    result.append(f"Current Recommendation : {recommendation}")
    result.append(f"Risk Level : {risk}")
    return result