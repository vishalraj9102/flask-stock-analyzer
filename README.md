# 📈 Flask Stock Analyzer

![Flask](https://img.shields.io/badge/Flask-Stock%20Analyzer-blue.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Render](https://img.shields.io/badge/Deployed%20on-Render-blue.svg)

A **Flask-based stock analysis** web application that fetches stock data and performs AI-driven analysis.

## 🚀 Live Demo
🔗 **[Flask Stock Analyzer](https://flask-stock-analyzer-hrc5.onrender.com/)** (Deployed on Render)

## 📂 Project Structure
```
flask-stock-analyzer/
│── app/
│   │── __init__.py
│   │── routes.py
│   │── ai_analysis.py
│   │── stock_data.py
│── config.py
│── requirements.txt
│── run.py
│── Dockerfile
│── vercel.json  (for Vercel Deployment)
│── render.yaml  (for Render Deployment)
│── README.md
```

## ⚙️ Installation

```sh
# Clone the repository
git clone https://github.com/vishalraj9102/flask-stock-analyzer.git
cd flask-stock-analyzer

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## ▶️ Running Locally
```sh
python run.py
```

Visit `http://127.0.0.1:5000/` in your browser.

## 📡 API Endpoints
### 🔍 Stock Analysis
**GET** `/analyze?ticker=AAPL`

#### Example Request:
```sh
curl -X GET "https://flask-stock-analyzer-hrc5.onrender.com/api/analyze?ticker=AAPL"
```
#### Example Response:
```json
{
  "ticker": "AAPL",
  "stock_info": { ... },
  "analysis": { ... }
}
```

## 🚀 Deploying on Render
1. Push changes to GitHub.
2. **Render Dashboard → Create New Web Service**
3. Connect your GitHub repository.
4. Set `Python 3.11` as the environment.
5. Auto-deploy on every push.

## 🛠️ Technologies Used
- **Flask** - Web Framework
- **Render** - Hosting Platform
- **AI/ML** - For Stock Analysis
