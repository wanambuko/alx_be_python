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
    current_dat_
