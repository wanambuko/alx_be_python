def safe_divide(numerator, denominator):
    """
    Perform division of numerator by denominator with robust error handling.
    
    Args:
        numerator (str or number): The numerator value.
        denominator (str or number): The denominator value.
    
    Returns:
        str: Result of division or an error message.
    """
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)
        
        # Attempt division
        try:
            result = num / denom
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
