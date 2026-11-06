from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def get_signal():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url).json()
    price = float(response['price'])
    signal = "BUY" if price > 0 else "SELL"
    return {"symbol": "BTCUSDT", "price": price, "signal": signal}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)