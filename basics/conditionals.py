"""
Python Conditionals - Basics
=============================

This script demonstrates if, elif, else statements and comparison operators.
"""

# Simple if statement
age = 18
if age >= 18:
    print("You are an adult!")

# If-else statement
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot.")

# If-elif-else statement
score = 85

if score >= 90:
    grade = "A"
    print(f"Excellent! Your grade is {grade}")
elif score >= 80:
    grade = "B"
    print(f"Good job! Your grade is {grade}")
elif score >= 70:
    grade = "C"
    print(f"Not bad! Your grade is {grade}")
elif score >= 60:
    grade = "D"
    print(f"You passed. Your grade is {grade}")
else:
    grade = "F"
    print(f"You need to improve. Your grade is {grade}")

# Comparison operators
a = 10
b = 20

print("\n=== Comparison Operators ===")
print(f"a == b: {a == b}")  # Equal to
print(f"a != b: {a != b}")  # Not equal to
print(f"a < b: {a < b}")    # Less than
print(f"a > b: {a > b}")    # Greater than
print(f"a <= b: {a <= b}")  # Less than or equal to
print(f"a >= b: {a >= b}")  # Greater than or equal to

# Logical operators
x = 5
y = 10

print("\n=== Logical Operators ===")
print(f"x > 0 and y > 0: {x > 0 and y > 0}")  # AND
print(f"x > 10 or y > 10: {x > 10 or y > 10}")  # OR
print(f"not x > 10: {not x > 10}")  # NOT

# Nested conditionals
username = "admin"
password = "secret123"

print("\n=== Nested Conditionals ===")
if username == "admin":
    if password == "secret123":
        print("Access granted!")
    else:
        print("Incorrect password!")
else:
    print("User not found!")

# Ternary operator (conditional expression)
age = 20
status = "adult" if age >= 18 else "minor"
print(f"\nAge {age}: Status is {status}")

# Check if value is in a list
fruits = ["apple", "banana", "orange"]
if "banana" in fruits:
    print("\nBanana is in the fruits list!")

if "grape" not in fruits:
    print("Grape is not in the fruits list!")

