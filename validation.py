def weight_validation():
    while True:
        weight = float(input("\nEnter weight(in kg): "))
        if weight <= 0:
            print(f"\nYou entered weight: {weight}")
            print("Weight can't be negative or zero")
            continue

        if weight > 1000:
            print(f"\nYou entered weight: {weight}")
            print("Weight seems in gram")
            while True:
                print("\nSelect one choice:")
                print("1. Convert weight in kg")
                print("2. Constinue with this value")
                print("3. Re enter value")
                choice = input("\nChoose 1, 2 or 3: ")
                if choice in ["1", "2", "3"]:
                    break
                print("\nYou have entered wrong number, please select from 1, 2 or 3")

            if choice == "1":
                new_weight = weight / 1000
                print(f"\nThe new weight is {new_weight}")
                while True:
                    print("1. Continue with this value")
                    print("2. Re enter weight")
                    confirm = input("Choose 1 or 2: ")
                    if confirm in ["1", "2"]:
                        break
                    print("\nYou have entered wrong choice. please select 1 or 2")
                if confirm == "1":
                    return new_weight
                else:
                    continue
            elif choice == "2":
                return weight
            else:
                continue
        
        if weight < 2:
            print(f"\nYou entered weight: {weight}")
            print("Weight seems low")
            while True:
                print("1. Continue with this weight")  
                print("2. Re enter")
                choice = input("\nEnter 1 or 2: ")
                if choice in ["1", "2"]:
                    break
                print("\nYou have entered wrong choice, please select 1 or 2")
            if choice == "1":
                return weight
            else:
                continue

        else:
            print(f"\nYou have entered weight: {weight}")   
            while True:
                print("1. Continue with this weight")
                print("2. Re enter weight")
                choice = input("\nChoose 1 or 2: ")
                if choice in ["1", "2"]:
                    break
                print("\nYou entered wrong choice, please select 1 or 2")
            if choice == "1":
                return weight
            else:
                continue      

def height_validation():
    while True:
        height = float(input("\nEnter your height(in m): "))
        if height <= 0:
            print(f"You have entered height: {height}")
            print("Height can't be negative or zero")
            continue
        
        if height > 3:
            print(f"\nYou have entered height: {height}")
            print("Quite high value of height")
            while True:
                print("1. Convert into meter")
                print("2. Continue with this height")
                print("3. Re enter Height")
                choice = input("\nChoose 1, 2 or 3: ")
                if choice in ["1", "2", "3"]:
                    break
                print("\nYou have chosen wrong choice, please enter 1, 2 or 3")

            if choice == "1":
                new_height = height / 100
                print(f"\nThe height in meter is {new_height}")
                while True:
                    print("1. Continue with this height")
                    print("2. Re enter height")
                    confirm = input("\nChoose 1 or 2: ")
                    if confirm in ["1", "2"]:
                        break
                    print("\nYou have entered wrong value, please enter 1 or 2")
                if confirm == "1":
                    return new_height
                else:
                    continue
            elif choice == "2":
                return height
            else:
                continue
        
        if height < 0.5:
            print(f"\nYou have entered height: {height}")
            print("Height seems quite less")
            while True:
                print("1. Continue with this height")
                print("2. Re enter Height")
                choice = input("\nChoose 1 or 2: ")
                if choice in ["1", "2"]:
                    break
                print("\nYou have entered wrong choice, please enter 1 or 2")
            if choice == "1":
                return height
            else:
                continue
        
        else:
            print(f"\nYou have entered height: {height}")
            while True:
                print("1. Continue with this height")
                print("2. Re enter height")
                choice = input("\nChoose 1 or 2: ")
                if choice in ["1", "2"]:
                    break
                print("\nYou have entered wrong choice, please enter 1 or 2")
            if choice == "1":
                return height
            else:
                continue

def name_validation():     
    while True:
        name = input("\nEnter your name: ").strip() 
        if name == "":
            print("Name can't be empty")
            continue
        if name.replace(" ","").isalpha():
            return name.title()
        else:
            print("Name can only contain alphabets and spaces.")

def food_name_validation():
    while True:
        food_name = input("\nEnter name of the food: ").strip()
        if food_name == "":
            print("Food name can't be empty")
            continue
        if food_name.replace(" ", "").isalpha():
            return food_name.lower()
        else:
            print("Food name can only contain alphabets and spaces")

def age_validation():
    while True:
        age = int(input("\nEnter your age: "))
        if age <= 0:
            print("Age can't be zero or negative")
            continue
        if age > 120:
            print("Please enter a realistic age")
            continue
        return age


def nutrition_validation(nutrient_name):
    while True:
        value = float(input(f"\nEnter {nutrient_name} per 100 grams: "))
        if value < 0:
            print(f"{nutrient_name} can't be negative.")
            continue
        return value

def quantity_validation():
    while True:
        quantity = float(input("\nEnter Quantity in grams: "))
        if quantity <= 0:
            print("\nQuantity must be greater than zero.")
            continue
        return quantity
    
def goal_validation():
    while True:
        print("\nSelect Goal:")
        print("1. Weight Loss")
        print("2. Weight Maintenance")
        print("3. Weight Gain")
        choice = input("\nChoose 1, 2 or 3: ")
        if choice in ["1", "2", "3"]:
            break
        print("\nYou have entered wrong choice, please enter 1, 2 or 3")
    if choice == "1":
        return "Weight Loss"
    if choice == "2":
        return "Weight Maintenance"
    if choice == "3":
        return "Weight Gain"
    
def gender_validation():
    while True:
        print("\nSelect gender:")
        print("1. Male")
        print("2. Female")
        print("3. Other")
        gender = input("\nChoose 1, 2 or 3: ")
        if gender in ["1", "2", "3"]:
            break
        print("\nYou have entered wrong, please select 1, 2 or 3")
    if gender == "1":
        return "Male"
    elif gender == "2":
        return "Female"
    elif gender == "3":
        return "Other"
    
def water_validation():
    while True:
        water = float(input("\nEnter water intake(in ml): "))
        if water <= 0:
            print("Water intake must be greater than zero.")
            continue
        return water
    
def sleep_validation():
    while True:
        sleep = float(input("\nEnter sleep hours: "))
        if sleep <= 0:
            print("\nSleep hours must be greater than zero.")
            continue
        if sleep > 24:
            print("\nA day has only 24 hours.")
            continue
        return sleep

def workout_duration_validation():
    while True:
        duration = int(input("\nEnter duration (in minutes): "))
        if duration <= 0:
            print("\nDuration must be greater than zero.")
            continue
        return duration
