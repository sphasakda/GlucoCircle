import requests

url = "http://127.0.0.1:5000/api/food/portion"

data = {
    "food_info": {
        "name": "Nutella",
        "calories": 539,
        "carbohydrates": 57.5,
        "protein": 6.3,
        "fat": 30.9,
        "fiber": 0,
        "sugars": 56.3
    },
    "portion_grams": 50
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.json())