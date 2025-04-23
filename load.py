import requests
import threading

def send_requests():
    while True:
        try:
            requests.get("http://localhost:5000/")
        except:
            pass

# Launch 10 threads to simulate load
threads = []
for _ in range(10):
    t = threading.Thread(target=send_requests)
    t.daemon = True
    t.start()

# Run for 60 seconds
import time
time.sleep(60)
