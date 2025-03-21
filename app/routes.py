from flask import Blueprint, request, jsonify
from app.stock_data import get_stock_data
from app.ai_analysis import analyze_data

stock_api = Blueprint('stock_api', __name__)

@stock_api.route('/analyze', methods=['GET'])
def analyze_stock():
    ticker = request.args.get('ticker')
    if not ticker:
        return jsonify({"error": "Ticker parameter is required"}), 400

    stock_info = get_stock_data(ticker)
    if "error" in stock_info:
        return jsonify(stock_info), 400

    analysis = analyze_data(stock_info)
    return jsonify({"ticker": ticker, "stock_info": stock_info, "analysis": analysis})
