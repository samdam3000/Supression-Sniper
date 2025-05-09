from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/live')
def live():
    return jsonify({
        "status": "Live endpoint working",
        "timestamp": time.time()
    })

@app.route('/trigger')
def trigger():
    return jsonify({
        "trigger": True,
        "confidence": "36.2%",
        "reason": "Suppression lifted: ineffective tackle + fast PTB",
        "time": time.strftime('%M:%S', time.gmtime(time.time() % 3600))
    })

if __name__ == '__main__':
    app.run(debug=True)
