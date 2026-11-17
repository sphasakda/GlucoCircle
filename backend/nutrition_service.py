import requests

# Barcode scanning function using the Open Food Facts API.
def get_food_by_barcode(barcode):
    url = f"https://world.openfoodfacts.org/api/v3/product/{barcode}.json"

    headers = {
        "User-Agent": "GlucoCircleApp/1.0 (sadphas17@gmail.com)"
    }
    response = requests.get(url, headers=headers, timeout=10)
    print("URL:", response.url)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text[:500])
    # Set a timeout of 10 seconds for the request to prevent hanging indefinitely in case of network issues or slow responses.

    if response.status_code != 200:
        return {"error": f"API request failed with status code {response.status_code}"}

    data = response.json()
    if data.get("status") != "success":
        return {"error": "Product not found"}

# Extract relevant nutritional information from the API response
    product = data.get("product", {})
    nutriments = product.get("nutriments", {})
    return {
        "name": product.get("product_name", "Unknown"),
        "brand": product.get("brands", "Unknown"),
        "calories": nutriments.get("energy-kcal_100g"),
        "carbohydrates": nutriments.get("carbohydrates_100g"),
        "protein": nutriments.get("proteins_100g"),
        "fat": nutriments.get("fat_100g"),
        "fiber": nutriments.get("fiber_100g"),
        "sugars": nutriments.get("sugars_100g"),
        "ingredients": product.get("ingredients_text", "Unknown"),
        "allergens": product.get("allergens", "Unknown"),
    }