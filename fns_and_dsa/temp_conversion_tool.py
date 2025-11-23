# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

# User interaction
def main():
    # Input temperature
    temp = input("Enter the temperature to convert: ")
    
    # Validate numeric input
    try:
        temp_value = float(temp)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Input unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    # Conversion
    if unit == "F":
        print(f"{temp_value}°F is {convert_to_celsius(temp_value)}°C")
    elif unit == "C":
        print(f"{temp_value}°C is {convert_to_fahrenheit(temp_value)}°F")
    else:
        print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")

if __name__ == "__main__":
    main()
