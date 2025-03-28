from flask import Flask
from app.routes import stock_api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(stock_api, url_prefix="/api")  # Add URL Prefix
    return app
