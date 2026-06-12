from validation import *
from food_database import *
from calculations import *
from fitness_database import *

user_profile = {}
all_users = {}
daily_meals = {
    "breakfast": [],
    "lunch": [],
    "dinner": [],
    "snacks": []
}

daily_water = 0
sleep_hours = 0
daily_workouts = []

def create_profile():
    global user_profile
    print("\n===============CREATE PROFILE===============")
    name = name_validation()
    if name in all_users:
        print("\nUser already exists.")
        return
    user_profile = {
        "name": name,
        "age": age_validation(),
        "gender": gender_validation(),
        "weight": weight_validation(),
        "height": height_validation(),
        "goal": goal_validation()
    }
    all_users[user_profile["name"]] = {"profile": user_profile}
    print("\nUser profile created successfully!")

def view_profile():
    if not user_profile:
        print("\nProfile not found")
        return
    print("\n===============USER PROFILE===============")
    print(f"\nName: {user_profile['name']}")
    print(f"Age: {user_profile['age']}")
    print(f"Gender: {user_profile['gender']}")
    print(f"Weight: {user_profile['weight']}")
    print(f"Height: {user_profile['height']}")
    print(f"Goal: {user_profile['goal']}")


def log_meal():
    if not user_profile:
        print("\nPlease create a profile first.")
        return
    print("\n===============SELECT MEALS===============")
    print("1. Breakfast")
    print("2. Lunch")
    print("3. Dinner")
    print("4. Snacks")
    while True:
        choice = input("\nChoose 1, 2, 3 or 4: ")
        if choice in ["1", "2", "3", "4"]:
            break
        print("Invalid choice")
    if choice == "1":
        meal_type = "breakfast"
    elif choice == "2":
        meal_type = "lunch"
    elif choice == "3":
        meal_type = "dinner"
    else:
        meal_type = "snacks"
    food_name = food_name_validation()
    if not search_food(food_name):
        print("\nFOOD NOT FOUND IN THE DATABASE, YOU CAN ADD USING - 7) ADD FOOD")
        return
    quantity = quantity_validation()
    daily_meals[meal_type].append({"food": food_name,"quantity": quantity})
    print(f"{food_name.title()} added to {meal_type.title()}")

def view_meals():
    if not user_profile:
        print("\nPlease create a profile first.")
        return
    print("\n===============DAILY MEALS===============")
    for meal in daily_meals:
        print(f"{meal.upper()}")
        if not daily_meals[meal]:
            print("No foods logged.")
            continue
        for item in daily_meals[meal]:
            calories = calculate_food_calories(item["food"],item["quantity"])
            protein = calculate_food_protein(item["food"], item["quantity"])
            print(f"{item['food'].title()} - {item['quantity']} g - {calories} Calories - {protein} Protein")


def bmi_analysis():
    if not user_profile:
        print("\nPlease create a profile first.")
        return
    bmi = calculate_bmi(user_profile["weight"],user_profile["height"])
    category = bmi_category(bmi)
    print(f"\nBMI: {bmi:.2f}")
    print(f"Category: {category}")

def nutrition_summary():
    if not user_profile:
        print("\nPlease create a profile first.")
        return
    calories = calculate_total_calories(daily_meals)
    protein = calculate_total_protein(daily_meals)
    carbs = calculate_total_carbs(daily_meals)
    fat = calculate_total_fat(daily_meals)
    calories_burned = calculate_total_calories_burned(daily_workouts)
    net_calories = calories - calories_burned
    print("\n==========DAILY NUTRITION SUMMARY==========")
    print(f"\nCalories Consumed: {calories:.2f} kcal")
    print(f"Calories Burned: {calories_burned:.2f} kcal")
    print(f"Net Calories: {net_calories:.2f} kcal")
    print(f"Protein: {protein:.2f} g")
    print(f"Carbs: {carbs:.2f} g")
    print(f"Fat: {fat:.2f} g")
    print(f"Water Intake: {daily_water} ml")
    print(f"Sleep Hours: {sleep_hours}")
    print(f"Sleep Status: {sleep_analysis()}")
    recommendation = diet_recommendation(
    user_profile["goal"],
    calories
    )
    print(f"Recommendation: {recommendation}")

def log_water():
    global daily_water
    if not user_profile:
        print("\nPlease create a profile first.")
        return
    water = water_validation()
    daily_water += water
    print(f"\n{water} ml added successfully.")
    print(f"Total water intake today: {daily_water} ml")

def log_sleep():
    global sleep_hours
    if not user_profile:
        print("\nPlease create a profile first.")
        return
    sleep_hours = sleep_validation()
    print(
        f"\nSleep duration recorded: {sleep_hours} hours"
    )

def sleep_analysis():
    if sleep_hours == 0:
        return "Not Recorded"
    if sleep_hours < 6:
        return "Insufficient Sleep"
    elif sleep_hours < 8:
        return "Adequate Sleep"
    else:
        return "Excellent Sleep"

def display_workouts():
    print("\n===============AVAILABLE WORKOUTS===============\n")
    count = 1
    for workout in workout_database:
        print(f"{count}. {workout.title()}")
        count += 1

def log_workout():
    if not user_profile:
        print("\nPlease create a profile first.")
        return
    display_workouts()
    workout_name = input("\nEnter workout name: ").lower()
    if not search_workout(workout_name):
        print("\nWorkout not found.")
        return
    duration = workout_duration_validation()
    daily_workouts.append({ "workout": workout_name, "duration": duration})
    print(f"\n{workout_name.title()} added successfully.")

def view_workouts():
    if not daily_workouts:
        print("\nNo workouts logged.")
        return
    print("\n=============TODAY'S WORKOUTS=============\n")
    for workout in daily_workouts:
        calories = calculate_workout_calories(workout["workout"], workout["duration"])
        print(f"{workout['workout'].title()} | Duration: {workout['duration']} min | Calories Burned: {calories} kcal")


def view_all_users():
    if not all_users:
        print("\nNo users found.")
        return

    print("\n=============== REGISTERED USERS ===============")
    print(f"\nTotal Registered Users: {len(all_users)}\n")

    count = 1
    for user in all_users:
        profile = all_users[user]["profile"]

        print(f"User {count}")
        print("-" * 40)
        print(f"Name   : {profile['name']}")
        print(f"Age    : {profile['age']}")
        print(f"Gender : {profile['gender']}")
        print(f"Weight : {profile['weight']} kg")
        print(f"Height : {profile['height']} m")
        print(f"Goal   : {profile['goal']}")
        print("-" * 40)
        print()

        count += 1


def health_score():
    score = 0
    bmi = calculate_bmi(user_profile["weight"], user_profile["height"])
    bmi_status = bmi_category(bmi)
    if daily_water >= 2000:
        score += 1
    if sleep_hours >= 7:
        score += 1
    if len(daily_workouts) > 0:
        score += 1
    if bmi_status == "Normal Weight":
        score += 1
    return score

def health_rating():
    score = health_score()
    if score == 4:
        return "Excellent"
    elif score == 3:
        return "Good"
    elif score == 2:
        return "Average"
    else:
        return "Needs Improvement"
    
def health_report():
    if not user_profile:
        print("\nPlease create a profile first.")
        return
    bmi = calculate_bmi(user_profile["weight"], user_profile["height"])
    bmi_status = bmi_category(bmi)
    print("\n===============DAILY HEALTH REPORT===============")
    print(f"BMI: {bmi:.2f}")
    print(f"BMI Category: {bmi_status}")
    print()
    print("-" * 30)
    print(f"Water Goal (2000 ml): {'Accomplished' if daily_water >= 2000 else 'Not Accomplished'}")
    print(f"Sleep Goal (7 hrs): {'Accomplished' if sleep_hours >= 7 else 'Not Accomplished'}")
    print(f"Workout Completed: "f"{'Yes' if len(daily_workouts) > 0 else 'No'}")
    print(f"BMI Normal: "f"{'Yes' if bmi_status == 'Normal Weight' else 'No'}")
    print("\nHealth Score:", health_score(), "/ 4")
    print("Health Rating:", health_rating())

def daily_dashboard():
    if not user_profile:
        print("\nPlease create a profile first.")
        return
    calories = calculate_total_calories(daily_meals)
    protein = calculate_total_protein(daily_meals)
    carbs = calculate_total_carbs(daily_meals)
    fat = calculate_total_fat(daily_meals)
    calories_burned = calculate_total_calories_burned(daily_workouts)
    net_calories = calories - calories_burned
    bmi = calculate_bmi(user_profile["weight"], user_profile["height"])
    bmi_status = bmi_category(bmi)
    print("\n" + "=" * 55)
    print("              DAILY HEALTH DASHBOARD")
    print("=" * 55)
    print("\nPROFILE:\n")
    print(f"Name: {user_profile['name']}")
    print(f"Goal: {user_profile['goal']}")
    print("\n" + "-" * 55)
    print("\nNUTRITION:\n")
    print(f"Calories Consumed: {calories:.2f} kcal")
    print(f"Calories Burned: {calories_burned:.2f} kcal")
    print(f"Net Calories: {net_calories:.2f} kcal")
    print(f"Protein: {protein:.2f} g")
    print(f"Carbs: {carbs:.2f} g")
    print(f"Fat: {fat:.2f} g")
    print("\n" + "-" * 55)
    print("\nHYDRATION & SLEEP:\n")
    print(f"Water Intake: {daily_water} ml")
    print(f"Sleep Hours: {sleep_hours}")
    print("\n" + "-" * 55)
    print("\nWORKOUTS:\n")
    if not daily_workouts:
        print("No workouts logged.")
    else:
        for workout in daily_workouts:
            calories_workout = calculate_workout_calories(workout["workout"], workout["duration"])
            print(f"{workout['workout'].title()} | Duration: {workout['duration']} min | Calories Burned: {calories_workout} kcal")
    print("\n" + "-" * 55)
    print("\nHEALTH STATUS:\n")
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {bmi_status}")
    print(f"Health Score: {health_score()}/4")
    print(f"Health Rating: {health_rating()}")
    print("\nSUGGESTIONS:\n")
    for suggestion in health_suggestions():
        print(f"- {suggestion}")
    print("\n" + "=" * 55)

def health_suggestions():
    suggestions = []
    if daily_water < 2000:
        suggestions.append("Drink more water to reach daily hydration goal.")
    if sleep_hours < 7:
        suggestions.append("Try getting at least 7 hours of sleep.")
    if len(daily_workouts) == 0:
        suggestions.append("Consider adding some physical activity today.")
    bmi = calculate_bmi(user_profile["weight"], user_profile["height"])
    bmi_status = bmi_category(bmi)
    if bmi_status == "Underweight":
        suggestions.append("Increase healthy calorie intake.")
    elif bmi_status == "Over Weight":
        suggestions.append("Focus on calorie control and exercise.")
    elif bmi_status == "Obese":
        suggestions.append("Consult a fitness or nutrition expert.")
    if not suggestions:
        suggestions.append("Excellent job! Keep maintaining your healthy lifestyle.")
    return suggestions

while True:
    print("\n===============MAIN MENU===============")
    print("\n1. Create Profile")
    print("2. View Profile")
    print("3. Log Meal")
    print("4. View Meals")
    print("5. BMI Analysis")
    print("6. Nutrition Summary")
    print("7. Add Food")
    print("8. View Food Database")
    print("9. Log Water Intake")
    print("10. Log Sleep")
    print("11. Log Workout")
    print("12. View Workouts")
    print("13. View All Users")
    print("14. Daily Health Report")
    print("15. Daily Dashboard")
    print("16. Exit")
    choice = input("\nChoose an option: ")
    if choice == "1":
        create_profile()
    elif choice == "2":
        view_profile()
    elif choice == "3":
        log_meal()
    elif choice == "4":
        view_meals()
    elif choice == "5":
        bmi_analysis()
    elif choice == "6":
        nutrition_summary()
    elif choice == "7":
        add_food()
    elif choice == "8":
        display_foods()
    elif choice == "9":
        log_water()
    elif choice == "10":
        log_sleep()
    elif choice == "11":
        log_workout()
    elif choice == "12":
        view_workouts()
    elif choice == "13":
        view_all_users()
    elif choice == "14":
        health_report()
    elif choice == "15":
        daily_dashboard()
    elif choice == "16":
        print("Thankyou")
        break
    else:
        print("Invalid choice.")



