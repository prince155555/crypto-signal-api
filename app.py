from flask import Flask
import requests

app = Flask(name)

@app.route('/')
def get_signal():
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = requests.get(url).json()
        price = float(response.get('price', 0))
        signal = "BUY" if price > 0 else "SELL"
        return {"symbol": "BTCUSDT", "price": price, "signal": signal}
    except Exception as e:
        return {"error": str(e)}, 500

if name == 'main':
    app.run(host='0.0.0.0', port=10000)