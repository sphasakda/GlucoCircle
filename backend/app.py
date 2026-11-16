#test endpoint for backend

from flask import Flask, jsonify

# Initialize Flask application
app = Flask(__name__)

# Test endpoint
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to GlucoseGuard!",
        "status": "Backend is running"
    })


# Start development server
if __name__ == "__main__":
    app.run(debug=True)
