import time
from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

ready = True

@app.route('/health')
def health():
    return "OK", 200

@app.route('/ready')
def readiness():
    global ready
    if ready:
        return "Ready", 200
    return "Not ready", 503

@app.route('/')
def index():
    global ready
    if not ready:
        time.sleep(10)  # Simulate app setup
        ready = True

    try:
        count = r.incr('hits')
    except redis.exceptions.ConnectionError:
        count = "Cannot connect to Redis"
    return f"Hello from v3 with probes! Visits: {count}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
