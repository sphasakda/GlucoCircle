#testing the nutrition service
from backend.nutrition_service import get_food_by_barcode

result = get_food_by_barcode("3017620422003")
print(result)