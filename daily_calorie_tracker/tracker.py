# -----------------------------------------------
# Name: Anshuman Sharma
# Date: 10 Nov 2025
# Project: Daily Calorie Tracker CLI
# -----------------------------------------------

print("Welcome to the Daily Calorie Tracker!")
print("This tool helps you record your meals and calculate your total calorie intake.\n")

# -------------------------------
# Task 2: Input & Data Collection
# -------------------------------

meal_names = []
meal_calories = []

num_meals = int(input("How many meals do you want to enter? "))

for i in range(num_meals):
    print(f"\nMeal {i+1}:")
    meal = input("Enter meal name: ")
    calories = float(input("Enter calories for this meal: "))

    meal_names.append(meal)
    meal_calories.append(calories)

# -------------------------------
# Task 3: Calorie Calculations
# -------------------------------

total_calories = sum(meal_calories)
average_calories = total_calories / num_meals

daily_limit = float(input("\nEnter your daily calorie limit: "))

# -------------------------------
# Task 4: Warning System
# -------------------------------

if total_calories > daily_limit:
    limit_msg = "⚠️ WARNING: You exceeded your daily calorie limit!"
else:
    limit_msg = "✔ You are within your daily calorie limit."

# -------------------------------
# Task 5: Neatly Formatted Output
# -------------------------------

print("\n\n----- DAILY CALORIE SUMMARY -----")
print("Meal Name\tCalories")
print("----------------------------------")

for i in range(num_meals):
    print(f"{meal_names[i]}\t\t{meal_calories[i]}")

print("----------------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")
print("----------------------------------")
print(limit_msg)

# -------------------------------
# Task 6: Bonus - Save to File
# -------------------------------

save = input("\nDo you want to save this session log? (yes/no): ")

if save.lower() == "yes":
    import datetime
    timestamp = datetime.datetime.now()

    with open("calorie_log.txt", "w") as file:
        file.write("----- DAILY CALORIE SUMMARY -----\n")
        file.write(f"Timestamp: {timestamp}\n\n")
        file.write("Meal Name\tCalories\n")
        file.write("---------------------------------\n")

        for i in range(num_meals):
            file.write(f"{meal_names[i]}\t\t{meal_calories[i]}\n")

        file.write("---------------------------------\n")
        file.write(f"Total:\t\t{total_calories}\n")
        file.write(f"Average:\t{average_calories:.2f}\n")
        file.write("---------------------------------\n")
        file.write(limit_msg + "\n")

    print("Session saved to calorie_log.txt")