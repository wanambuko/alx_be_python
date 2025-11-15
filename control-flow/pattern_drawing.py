# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Outer while loop for rows
while row < size:
    # Inner for loop for columns
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line after a row is complete
    row += 1  # Increment row counter
