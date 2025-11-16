"""
Python Variables - Basics
==========================

This script demonstrates various types of variables in Python.
"""

# Integer variables
age = 25
temperature = -10
score = 100

# Float variables
height = 5.9
pi = 3.14159
price = 19.99

# String variables
name = "Alice"
greeting = 'Hello, World!'
message = """This is a multi-line
string in Python"""

# Boolean variables
is_student = True
is_employed = False
has_license = True

# List variables
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
mixed_list = [1, "hello", 3.14, True]

# Dictionary variables
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Tuple variables
coordinates = (10, 20)
rgb_color = (255, 128, 0)

# Set variables
unique_numbers = {1, 2, 3, 4, 5}
vowels = {'a', 'e', 'i', 'o', 'u'}

# Displaying variables
print("=== Python Variables Demo ===\n")
print(f"Integer: age = {age}")
print(f"Float: height = {height}")
print(f"String: name = {name}")
print(f"Boolean: is_student = {is_student}")
print(f"List: numbers = {numbers}")
print(f"Dictionary: person = {person}")
print(f"Tuple: coordinates = {coordinates}")
print(f"Set: unique_numbers = {unique_numbers}")

# Variable reassignment
x = 10
print(f"\nInitial value of x: {x}")
x = 20
print(f"After reassignment, x = {x}")

# Multiple assignment
a, b, c = 1, 2, 3
print(f"\nMultiple assignment: a={a}, b={b}, c={c}")

# Type checking
print(f"\nType of age: {type(age)}")
print(f"Type of name: {type(name)}")
print(f"Type of is_student: {type(is_student)}")

