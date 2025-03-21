import yfinance as yf

def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        return {
            "name": info.get("longName", "N/A"),
            "sector": info.get("sector", "N/A"),
            "marketCap": info.get("marketCap", "N/A"),
            "currentPrice": info.get("currentPrice", "N/A"),
            "52WeekHigh": info.get("fiftyTwoWeekHigh", "N/A"),
            "52WeekLow": info.get("fiftyTwoWeekLow", "N/A"),
            "peRatio": info.get("trailingPE", "N/A"),
        }
    except Exception as e:
        return {"error": str(e)}
