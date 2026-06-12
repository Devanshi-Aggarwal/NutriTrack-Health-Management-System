from validation import *

food_database = {
    "apple": {
        "calories": 52,
        "protein": 0.3,
        "carbs": 13.8,
        "fat": 0.2
    },
    "banana": {
        "calories": 89,
        "protein": 1.1,
        "carbs": 22.8,
        "fat": 0.3
    },
    "orange": {
        "calories": 47,
        "protein": 0.9,
        "carbs": 11.8,
        "fat": 0.1
    },
    "milk": {
        "calories": 61,
        "protein": 3.2,
        "carbs": 4.8,
        "fat": 3.3
    },
    "curd": {
        "calories": 70,
        "protein": 3.5,
        "carbs": 5.3,
        "fat": 3.5
    },
    "egg": {
        "calories": 143,
        "protein": 12.6,
        "carbs": 0.7,
        "fat": 9.5
    },
    "paneer": {
        "calories": 265,
        "protein": 18.3,
        "carbs": 3.2,
        "fat": 20.1
    },
    "chicken": {
        "calories": 120,
        "protein": 22.5,
        "carbs": 0.0,
        "fat": 2.6
    },
    "rice": {
        "calories": 130,
        "protein": 2.7,
        "carbs": 28.0,
        "fat": 0.3
    },
    "chapati": {
        "calories": 275,
        "protein": 9.3,
        "carbs": 56.0,
        "fat": 1.4
    },
    "oats": {
        "calories": 389,
        "protein": 13.6,
        "carbs": 67.7,
        "fat": 6.8
    },
    "bread": {
        "calories": 265,
        "protein": 9.0,
        "carbs": 49.0,
        "fat": 3.2
    },
    "potato": {
        "calories": 77,
        "protein": 2.0,
        "carbs": 17.0,
        "fat": 0.1
    },
    "tomato": {
        "calories": 18,
        "protein": 0.9,
        "carbs": 3.9,
        "fat": 0.2
    },
    "onion": {
        "calories": 40,
        "protein": 1.1,
        "carbs": 9.3,
        "fat": 0.1
    },
    "dal": {
        "calories": 116,
        "protein": 9.0,
        "carbs": 20.0,
        "fat": 0.4
    },
    "almonds": {
        "calories": 579,
        "protein": 21.2,
        "carbs": 21.6,
        "fat": 49.9
    },
    "peanuts": {
        "calories": 567,
        "protein": 25.8,
        "carbs": 16.1,
        "fat": 49.2
    },
    "broccoli": {
        "calories": 34,
        "protein": 2.8,
        "carbs": 6.6,
        "fat": 0.4
    },
    "carrot": {
        "calories": 41,
        "protein": 0.9,
        "carbs": 9.6,
        "fat": 0.2
    }
}


def display_foods():
    print("\nAVAILABLE FOODS: ")
    count = 1
    for food in food_database:
        print(f"{count}. {food.title()}")
        count += 1

def search_food(food_name):
    food_name = food_name.lower()
    return food_name in food_database

def view_food_details(food_name):
    food_name = food_name.lower()
    if food_name not in food_database:
        print("\nFood not found")
        return
    print(f"Food: {food_name.title()}")
    print(f"Calories: {food_database[food_name]['calories']}")
    print(f"Protein: {food_database[food_name]['protein']} g")
    print(f"Carbs: {food_database[food_name]['carbs']} g")
    print(f"Fat: {food_database[food_name]['fat']} g")
 
def add_food():
    food_name = food_name_validation()
    if food_name in food_database:
        print(f"\n{food_name.title()} already exists in the database")
        return
    calories = nutrition_validation("Calories")
    protein = nutrition_validation("Protein")
    carbs = nutrition_validation("Carbs")
    fat = nutrition_validation("Fat")
    food_database[food_name] = {"calories": calories, "protein": protein, "carbs": carbs, "fat": fat}
    print(f"\n{food_name.title()} added successfully!")

