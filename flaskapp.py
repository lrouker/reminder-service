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
    response = reminders.add_to_redis(r, data)
    if response == 0:
        return "Accepted"
    else:
        return "Error, please try again"  # In an actual workflow, we'd spit out some error coding / support to contact / where to report a bug

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')