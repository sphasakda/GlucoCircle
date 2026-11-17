#testing the nutrition service
from backend.nutrition_service import (
    get_food_by_barcode,
    calculate_portion_nutrition, search_food
)

if __name__ == "__main__":

    # Barcode lookup
    food_info = get_food_by_barcode("3017620422003")
    print("FOOD INFO:", food_info)

    # Portion validation tests
    print("50g:", calculate_portion_nutrition(food_info, 50))
    print("0g:", calculate_portion_nutrition(food_info, 0))
    print("-25g:", calculate_portion_nutrition(food_info, -25))
    print("Boolean:", calculate_portion_nutrition(food_info, True))

    # Incomplete nutrition data test
    incomplete_food_info = {
        "name": "Test Food",
        "brand": "Test Brand",
        "calories": 200,
        "carbohydrates": 30,
        "protein": 5,
        "fat": 8,
        "fiber": None,
        "sugars": None,
        "ingredients": "",
        "allergens": ""
    }

    print(
        "INCOMPLETE FOOD TEST:",
        calculate_portion_nutrition(incomplete_food_info, 50))
    print("FOOD SEARCH:", search_food("Nutella"))
