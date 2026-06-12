workout_database = {
    "walking": {"calories_per_minute": 4}, 
    "running": {"calories_per_minute": 10}, 
    "cycling": {"calories_per_minute": 8},
    "swimming": {"calories_per_minute": 11},
    "jump rope": {"calories_per_minute": 12},
    "yoga": {"calories_per_minute": 3},
    "strength training": {"calories_per_minute": 7},
    "dancing": {"calories_per_minute": 6},
    "hiking": {"calories_per_minute": 7},
    "badminton": {"calories_per_minute": 8},
    "football": {"calories_per_minute": 10}
    }

def search_workout(workout_name):
    workout_name = workout_name.lower()
    return workout_name in workout_database

