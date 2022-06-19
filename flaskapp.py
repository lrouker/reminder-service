from flask import Flask, request, jsonify
import reminders
app = Flask(__name__)
r = reminders.get_connection()

@app.route('/api/reminders', methods=['GET'])
def handle_get():
    return jsonify(reminders.get_all(r))

@app.route('/api/reminders', methods=['POST'])
def handle_post():
    data = request.data
    return reminders.add_to_redis(r, data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')