from flask import Flask, jsonify, request
from mock_data import generate_glucose_data
from glucose_analysis import analyze_glucose_readings
from ai_service import ask_claude

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

@app.route("/api/analysis", methods=["GET"])
def get_glucose_analysis():
    readings = generate_glucose_data()
    analysis_results = analyze_glucose_readings(readings)

    return jsonify({
        "analysis": analysis_results
    })

# AI assistant endpoint (Claude call lives in ai_service.py)
@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_message = data.get("message", "") if data else ""
    if not user_message:
        return jsonify({"error": "message is required"}), 400
    try:
        reply = ask_claude(user_message)
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start development server
if __name__ == "__main__":
    app.run(debug=True)