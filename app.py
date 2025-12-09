from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import requests

app = Flask(__name__)
metrics = PrometheusMetrics(app) 

def get_temperature():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 52.52,      
        "longitude": 13.41,    
        "current_weather": True
    }
    r = requests.get(url, params=params, timeout=3)
    data = r.json()
    return data["current_weather"]["temperature"]

@app.get("/")
def temperature():
    return jsonify({
        "city": "Berlin",
        "temp_c": get_temperature()
    })

@app.get("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
