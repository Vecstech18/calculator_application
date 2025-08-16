def calculator_floor_division(num1, num2):
    """
    Performs floor division on two numbers.

    Args:
        num1 (int or float): The dividend.
        num2 (int or float): The divisor.

    Returns:
        int or float: The result of the floor division.
                      Returns an error message if division by zero occurs.
    """
    if num2 == 0:
        return "Error: Cannot divide by zero."
    else:
        return num1 // num2

# Example usage:
result1 = calculator_floor_division(15, 4)
print(f"Floor division of 15 by 4: {result1}")

result2 = calculator_floor_division(10, 3)
print(f"Floor division of 10 by 3: {result2}")

result3 = calculator_floor_division(-7, 2)
print(f"Floor division of -7 by 2: {result3}")

result4 = calculator_floor_division(5, 0)
print(f"Floor division of 5 by 0: {result4}")
