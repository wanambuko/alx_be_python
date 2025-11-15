# daily_reminder.py

# Prompt user for task
task = input("Enter your task: ")

# Prompt for priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt for time-bound status
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task using match-case for priority
match priority:
    case "high":
        reminder = f"{task} is a high priority task"
    case "medium":
        reminder = f"{task} is a medium priority task"
    case "low":
        reminder = f"{task} is a low priority task"
    case _:
        reminder = f"{task} has an unspecified priority"

# Adjust message for time-bound tasks
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the reminder exactly as required
print(f"Reminder: {reminder}")
