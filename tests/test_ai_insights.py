print("AI Service Test Script")

from backend.mock_data import generate_glucose_data
from backend.glucose_analysis import analyze_glucose_readings
from backend.ai_service import generate_glucose_insights

readings = generate_glucose_data()
print("1. Generated glucose reading generated")

results = analyze_glucose_readings(readings)
print("2. Glucose analysis generated")

insights = generate_glucose_insights(results)
print("3. Claude response generated")

print(insights)
