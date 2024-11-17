# math_operations.py

def divide_numbers(a, b):
    """Divides two numbers and returns the result."""
    if b == 0:
        print("Division by zero is not allowed.")
        return "Undfined"  # Potential division by zero error
    return a / b  # Potential division by zero error

if __name__ == "__main__":
    x = 10
    y = 0
    result = divide_numbers(x, y)
    print(f"The result of division is: {result}")