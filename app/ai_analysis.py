import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_data(stock_info):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"""
        Analyze the following stock data:
        Name: {stock_info['name']}
        Sector: {stock_info['sector']}
        Market Cap: {stock_info['marketCap']}
        Current Price: {stock_info['currentPrice']}
        52 Week High: {stock_info['52WeekHigh']}
        52 Week Low: {stock_info['52WeekLow']}
        PE Ratio: {stock_info['peRatio']}

        Provide insights about the company’s financial health and investment potential.
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return {"error": str(e)}
