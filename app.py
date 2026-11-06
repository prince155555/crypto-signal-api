from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def get_signal():
    try:
        url = "https://blockchain.info/ticker"
        response = requests.get(url, timeout=5).json()
        price = float(response['USD']['last'])
        signal = "BUY" if price > 0 else "SELL"
        return {"symbol": "BTCUSDT", "price": price, "signal": signal}
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)