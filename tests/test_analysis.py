from backend.mock_data import generate_glucose_data
from backend.glucose_analysis import analyze_glucose_readings

results = analyze_glucose_readings(generate_glucose_data())
print(results)
