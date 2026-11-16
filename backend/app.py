from flask import Flask, jsonify
from mock_data import generate_glucose_data

# Initialize Flask application
app = Flask(__name__)

# Test endpoint
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to GlucoseGuard!",
        "status": "Backend is running"
    })

@app.route("/api/glucose", methods=["GET"])
def glucose():

    readings = generate_glucose_data()

    return jsonify({
        "source": "simulated",
        "total_readings": len(readings),
        "readings": readings
    })
# Start development server
if __name__ == "__main__":
    app.run(debug=True)
