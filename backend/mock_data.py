
from datetime import datetime, timedelta, timezone

def generate_glucose_data():

    # Synthetic glucose readings for development
    glucose_values = [
        105, 112, 118, 135,
        152, 165, 158, 143,
        130, 122, 115, 110
    ]

    readings = []

    current_time = datetime.now(timezone.utc)

    for i, value in enumerate(glucose_values):

        timestamp = current_time - timedelta(minutes=5 * (len(glucose_values) - 1 - i))

        readings.append({
            "timestamp": timestamp.isoformat(),
            "glucose": value,
            "unit": "mg/dL"
        })

    return readings
