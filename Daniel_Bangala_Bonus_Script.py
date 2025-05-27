from datetime import datetime

habits_list = []

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")

def add_habit():
    name = input("Enter the habit name: ")
    if name == "":
        print("Habit name cannot be empty.")
        return

    habit = {
        "name": name,
        "date": get_current_date(),
        "completed": False
    }

    habits_list.append(habit)
    print("Habit '" + name + "' added successfully.")
    print()

def view_habits():
    today = get_current_date()
    today_habits = []

    for habit in habits_list:
        if habit["date"] == today:
            today_habits.append(habit)

    if len(today_habits) == 0:
        print("No habits for today.")
        print()
    else:
        print("Today's Habits (" + today + "):")
        for h in today_habits:
            if h["completed"]:
                status = "X"
            else:
                status = "O"
            print(status + " " + h["name"])
        print()

def show_menu():
    while True:
        print("=== DAILY HABIT TRACKER ===")
        print("1. Add a habit")
        print("2. View habits")
        print("3. Exit")
        print()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_habit()
        elif choice == "2":
            view_habits()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            print()

show_menu()
