from statistics import mean, pstdev


def analyze_glucose_readings(readings):

    # Check whether readings exist
    if not readings:
        raise ValueError("No glucose readings provided")

    # Extract glucose values
    values = [reading["glucose"] for reading in readings]

    # Validate the measurements
    if any(
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        for value in values
    ):
        raise ValueError("Glucose readings must be numeric")

    if any(value <= 0 for value in values):
        raise ValueError("Glucose readings must be positive")

    # Calculate statistics
    average = mean(values)
    minimum = min(values)
    maximum = max(values)
    variability = pstdev(values)

    # Compare first and last readings
    glucose_change = values[-1] - values[0]

    if glucose_change > 0:
        direction = "increasing"
    elif glucose_change < 0:
        direction = "decreasing"
    else:
        direction = "unchanged"

    # Return analysis results
    return {
        "total_readings": len(values),
        "average_glucose": round(average, 2),
        "minimum_glucose": minimum,
        "maximum_glucose": maximum,
        "glucose_change": round(glucose_change, 2),
        "standard_deviation": round(variability, 2),
        "overall_direction": direction,
        "unit": "mg/dL"
    }
