# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    # Prompt user for temperature
    temp_input = input("Enter the temperature to convert: ")

    # Validate temperature input
    try:
        temp_value = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Ask for the unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Convert based on unit
    if unit == "F":
        converted = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {converted}°C")
    elif unit == "C":
        converted = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {converted}°F")
    else:
        print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")

if __name__ == "__main__":
    main()
