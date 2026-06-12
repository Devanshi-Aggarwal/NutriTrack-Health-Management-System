from food_database import *
from fitness_database import *

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Over Weight"
    else:
        return "Obese"
    

def calculate_food_calories(food_name, quantity):
    calories_per_100g = food_database[food_name]["calories"]
    calories = (quantity * calories_per_100g) / 100
    return calories

def calculate_food_protein(food_name, quantity):
    protein_per_100g = food_database[food_name]["protein"]
    protein = (quantity * protein_per_100g) / 100
    return protein

def calculate_food_carbs(food_name, quantity):
    carbs_per_100g = food_database[food_name]["carbs"]
    carbs = (quantity * carbs_per_100g) / 100
    return carbs

def calculate_food_fat(food_name, quantity):
    fat_per_100g = food_database[food_name]["fat"]
    fat = (quantity * fat_per_100g) / 100
    return fat

def calculate_total_calories(daily_meals):
    total_calories = 0
    for meal in daily_meals:
        for item in daily_meals[meal]:
            total_calories += calculate_food_calories(item["food"],item["quantity"])
    return total_calories

def calculate_total_protein(daily_meals):
    total_protein = 0
    for meal in daily_meals:
        for item in daily_meals[meal]:
            total_protein += calculate_food_protein(item["food"],item["quantity"])
    return total_protein

def calculate_total_carbs(daily_meals):
    total_carbs = 0
    for meal in daily_meals:
        for item in daily_meals[meal]:
            total_carbs += calculate_food_carbs(item["food"], item["quantity"])
    return total_carbs

def calculate_total_fat(daily_meals):
    total_fat = 0
    for meal in daily_meals:
        for item in daily_meals[meal]:
            total_fat += calculate_food_fat(item["food"],item["quantity"])
    return total_fat

def diet_recommendation(goal, calories):
    if goal == "Weight Loss":
        if calories > 1800:
            return "\nReduce calorie intake."
        elif calories < 1200:
            return "\nCalorie intake is very low."
        else:
            return "\nCalorie intake is within target."
    elif goal == "Weight Maintenance":
        if calories > 2200:
            return "\nCalorie intake is above maintenance."
        elif calories < 1800:
            return "\nCalorie intake is below maintenance."
        else:
            return "\nCalorie intake is within target."
    else:
        if calories < 2500:
            return "\nIncrease calorie intake."
        else:
            return "\nCalorie intake is within target."
        
def calculate_workout_calories(workout_name,duration):
    calories_per_minute = workout_database[workout_name]["calories_per_minute"]
    calories_burned = (calories_per_minute *duration)
    return calories_burned

def calculate_total_calories_burned(daily_workouts):
    total = 0
    for workout in daily_workouts:
        total += calculate_workout_calories(workout["workout"], workout["duration"])
    return total