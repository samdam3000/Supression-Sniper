from flask import Flask, jsonify
from suppression_engine import evaluate_trigger
from scraper import scrape_fox_sports
import time

app = Flask(__name__)

cached_data = None
last_updated = 0
CACHE_DURATION = 5

@app.route('/live')
def get_live_data():
    global cached_data, last_updated
    now = time.time()
    if cached_data and (now - last_updated) < CACHE_DURATION:
        return jsonify(cached_data)
    cached_data = scrape_fox_sports()
    last_updated = now
    return jsonify(cached_data)

@app.route('/trigger')
def trigger_check():
    result = evaluate_trigger()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
