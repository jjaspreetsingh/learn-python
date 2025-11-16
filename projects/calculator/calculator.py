"""
Simple Calculator Project
==========================

A command-line calculator that performs basic arithmetic operations.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def power(a, b):
    """Raise a to the power of b."""
    return a ** b

def calculator():
    """Main calculator function."""
    print("=== Simple Calculator ===")
    print("Operations: +, -, *, /, ^")
    print("Type 'quit' to exit\n")
    
    while True:
        try:
            # Get user input
            expression = input("Enter expression (e.g., 5 + 3): ").strip()
            
            if expression.lower() == 'quit':
                print("Goodbye!")
                break
            
            # Parse the expression
            parts = expression.split()
            if len(parts) != 3:
                print("Invalid format! Use: number operator number")
                continue
            
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
            
            # Perform calculation
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            elif operator == '^':
                result = power(num1, num2)
            else:
                print("Invalid operator! Use: +, -, *, /, ^")
                continue
            
            print(f"Result: {result}\n")
            
        except ValueError as e:
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")

if __name__ == "__main__":
    calculator()

