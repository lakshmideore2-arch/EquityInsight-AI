import yfinance as yf
def get_financial_statements(ticker):
    stock = yf.Ticker(ticker)
    financials = stock.financials
    balance_sheet = stock.balance_sheet
    cash_flow = stock.cashflow
    return (
        financials,
        balance_sheet,
        cash_flow
    )