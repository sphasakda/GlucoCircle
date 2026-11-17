from flask import Flask, jsonify, request
from backend.mock_data import generate_glucose_data
from backend.glucose_analysis import analyze_glucose_readings
from backend.ai_service import ask_claude
from backend.nutrition_service import (
    search_food,
    get_food_by_barcode,
    calculate_portion_nutrition)

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


# Search food by name
@app.route("/api/food/search", methods=["GET"])
def food_search():
    query = request.args.get("q", "").strip()

    if not query:
        return jsonify({"error": "Search query is required"}), 400

    results = search_food(query)

    if isinstance(results, dict) and "error" in results:
        return jsonify(results), 500

    return jsonify({
        "query": query,
        "results": results
    })


# Retrieve food information by barcode
@app.route("/api/food/barcode/<barcode>", methods=["GET"])
def food_barcode(barcode):
    food_info = get_food_by_barcode(barcode)

    if "error" in food_info:
        return jsonify(food_info), 404

    return jsonify(food_info)


# Calculate nutrition for a serving size
@app.route("/api/food/portion", methods=["POST"])
def food_portion():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    food_info = data.get("food_info")
    portion_grams = data.get("portion_grams")

    if not isinstance(food_info, dict):
        return jsonify({"error": "Food information is required"}), 400

    result = calculate_portion_nutrition(
        food_info,
        portion_grams
    )

    if "error" in result:
        return jsonify(result), 400

    return jsonify(result)

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