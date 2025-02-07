# backend/app.py
from flask import Flask, request, jsonify
from routing import calculate_route
from flask_cors import CORS

app = Flask(__name__)
CORS(app,origins=['*'])

@app.route('/calculate-route', methods=['POST'])
def calculate_route_api():
    data = request.get_json()
    start_coords = data.get('start_coords')
    end_coords = data.get('end_coords')

    if not start_coords or not end_coords :
        return jsonify({"error": "Start and end coords are required"}), 400

    route = calculate_route(start_coords, end_coords)
    return jsonify({'route': route})

@app.route('/')
def index():
    return "Server is running!"

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(host='0.0.0.0', debug=True, port=5001)