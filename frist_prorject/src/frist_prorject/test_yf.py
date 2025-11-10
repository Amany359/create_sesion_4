import yfinance as yf

data = yf.download("AAPL", period="1mo")
print(data.head())
