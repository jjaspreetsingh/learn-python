"""
Python Functions - Intermediate
=================================

This script demonstrates function definitions, parameters, return values, and advanced concepts.
"""

# Simple function
def greet():
    """Simple function that greets the user."""
    print("Hello, welcome to Python!")

print("=== Simple Function ===")
greet()

# Function with parameters
def greet_person(name):
    """Function that greets a specific person."""
    print(f"Hello, {name}! Nice to meet you.")

print("\n=== Function with Parameters ===")
greet_person("Alice")
greet_person("Bob")

# Function with multiple parameters
def introduce(name, age, city):
    """Function with multiple parameters."""
    print(f"Hi, I'm {name}, {age} years old, from {city}.")

print("\n=== Function with Multiple Parameters ===")
introduce("Charlie", 28, "London")

# Function with default parameters
def greet_with_time(name, time_of_day="morning"):
    """Function with default parameter."""
    print(f"Good {time_of_day}, {name}!")

print("\n=== Function with Default Parameters ===")
greet_with_time("David")
greet_with_time("Eve", "evening")

# Function with return value
def add(a, b):
    """Function that returns the sum of two numbers."""
    return a + b

print("\n=== Function with Return Value ===")
result = add(5, 3)
print(f"5 + 3 = {result}")

# Function with multiple return values
def get_name_and_age():
    """Function that returns multiple values."""
    name = "Frank"
    age = 35
    return name, age

print("\n=== Function with Multiple Return Values ===")
name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}")

# Function with keyword arguments
def create_profile(name, age, city, country):
    """Function demonstrating keyword arguments."""
    print(f"Profile: {name}, {age}, {city}, {country}")

print("\n=== Function with Keyword Arguments ===")
create_profile(name="Grace", city="Tokyo", country="Japan", age=29)

# Function with *args (variable arguments)
def sum_all(*numbers):
    """Function that accepts variable number of arguments."""
    total = 0
    for num in numbers:
        total += num
    return total

print("\n=== Function with *args ===")
print(f"Sum of 1, 2, 3 = {sum_all(1, 2, 3)}")
print(f"Sum of 1, 2, 3, 4, 5 = {sum_all(1, 2, 3, 4, 5)}")

# Function with **kwargs (keyword arguments dictionary)
def print_info(**kwargs):
    """Function that accepts variable keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\n=== Function with **kwargs ===")
print_info(name="Henry", age=42, occupation="Engineer")

# Lambda functions (anonymous functions)
print("\n=== Lambda Functions ===")
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

multiply = lambda x, y: x * y
print(f"3 * 4 = {multiply(3, 4)}")

# Using lambda with map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared}")

# Using lambda with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Nested functions
def outer_function(x):
    """Function containing a nested function."""
    def inner_function(y):
        return y * 2
    
    result = inner_function(x)
    return result + 10

print("\n=== Nested Functions ===")
print(f"outer_function(5) = {outer_function(5)}")

# Recursive function
def factorial(n):
    """Calculate factorial using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("\n=== Recursive Function ===")
print(f"Factorial of 5: {factorial(5)}")

# Function with type hints (Python 3.5+)
def calculate_area(length: float, width: float) -> float:
    """Function with type hints."""
    return length * width

print("\n=== Function with Type Hints ===")
area = calculate_area(5.5, 3.2)
print(f"Area: {area}")

