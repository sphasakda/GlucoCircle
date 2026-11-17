import requests

# Barcode scanning function using the Open Food Facts API.
def get_food_by_barcode(barcode):
    url = f"https://world.openfoodfacts.org/api/v3/product/{barcode}.json"

    headers = {
        "User-Agent": "GlucoCircleApp/1.0 (sadphas17@gmail.com)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
    except requests.Timeout:
        return {"error": "Food database request timed out. Please try again."}
    except requests.RequestException as error:
        return {"error": str(error)}

    if response.status_code != 200:
        return {"error": f"API request failed with status code {response.status_code}"}

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

#calculate the nutritional information based on portion size.
def calculate_portion_nutrition(food_info, portion_grams):
    if isinstance(portion_grams, bool) or not isinstance(portion_grams, (int, float)) or portion_grams <= 0:
        return {"error": "Portion size must be a number"}


    factor = portion_grams / 100.0
    return {
        "name": food_info.get("name"),
        "brand": food_info.get("brand"),
        "calories": round(food_info.get("calories") * factor, 2) if food_info.get("calories") is not None else None,
        "carbohydrates": round(food_info.get("carbohydrates") * factor, 2) if food_info.get("carbohydrates") is not None else None,
        "protein": round(food_info.get("protein") * factor, 2) if food_info.get("protein") is not None else None,
        "fat": round(food_info.get("fat") * factor, 2) if food_info.get("fat") is not None else None,
        "fiber": round(food_info.get("fiber") * factor, 2) if food_info.get("fiber") is not None else None,
        "sugars": round(food_info.get("sugars") * factor, 2) if food_info.get("sugars") is not None else None,
        "ingredients": food_info.get("ingredients"),
        "allergens": food_info.get("allergens"),
    }

#lookup function to search for food items by name using the Open Food Facts API.
def search_food(query):
    if not query or not query.strip():
        return {"error": "Search query cannot be empty"}

    url = "https://search.openfoodfacts.org/search"

    params = {
        "q": query.strip(),
        "page_size": 5
    }

    headers = {
        "User-Agent": "GlucoCircle/1.0"
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=15
        )
        response.raise_for_status()
        data = response.json()
        hits = data.get("hits", [])

        results = []

        for product in hits:
            nutriments = product.get("nutriments", {})

            # Skip products without calorie information
            if nutriments.get("energy-kcal_100g") is None:
                continue

            results.append({
                "name": product.get("product_name") or product.get("product_name_en") or "Unknown",
                "brand": product.get("brands"),
                "barcode": product.get("code"),
                "calories": nutriments.get("energy-kcal_100g"),
                "carbohydrates": nutriments.get("carbohydrates_100g"),
                "protein": nutriments.get("proteins_100g"),
                "fat": nutriments.get("fat_100g"),
                "fiber": nutriments.get("fiber_100g"),
                "sugars": nutriments.get("sugars_100g"),
                "image_url": product.get("image_url")
            })

        return results

    except requests.RequestException as error:
        return {"error": str(error)}
