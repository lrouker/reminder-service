from flask import Flask, request, jsonify
import redis, json, uuid
app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/api/reminders', methods=['GET'])
def handle_get():
    retList = []
    for key in r.scan_iter():
      retList.append(json.loads(r.get(key)))
    return jsonify(retList)

@app.route('/api/reminders', methods=['POST'])
def handle_post():
    data = request.data
    id = str(uuid.uuid1())
    r.mset({id: data})
    return "Accepted"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')