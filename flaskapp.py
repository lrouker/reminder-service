from flask import Flask, request
import redis
app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/api/reminders', methods=['GET'])
def handle_get():
    return r.get("reminder2")

@app.route('/api/reminders', methods=['POST'])
def handle_post():
    r.mset({"reminder1": "Hello", "reminder2": "World"})
    return "Hello world POST"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')