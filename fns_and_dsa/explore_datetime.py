from datetime import datetime, timedelta

# Part 1: Display Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # format date
    print(f"Current date and time: {formatted_date}")
    return formatted_date  # return the formatted string

# Part 2: Calculate Future Date
def calculate_future_date(current_date, days_to_add):
    # Convert string back to datetime object
    current_datetime = datetime.strptime(current_date, "%Y-%m-%d %H:%M:%S")
    future_date = current_datetime + timedelta(days=days_to_add)
    formatted_future = future_date.strftime("%Y-%m-%d")  # format future date
    print(f"Future date: {formatted_future}")
    return formatted_future  # return formatted string

def main():
    # Display current date and time
    current_date_str = display_current_datetime()

    # Ask user for number of days to add
    while True:
        try:
            days_input = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    # Calculate future date
    calculate_future_date(current_date_str, days_input)

if __name__ == "__main__":
    main()
