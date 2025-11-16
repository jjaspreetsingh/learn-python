"""
Python Loops - Basics
======================

This script demonstrates for loops, while loops, and loop control statements.
"""

# For loop with range
print("=== For Loop with Range ===")
for i in range(5):
    print(f"Count: {i}")

print("\nRange from 2 to 10:")
for i in range(2, 10):
    print(i, end=" ")
print()

print("\nRange with step size of 2:")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# For loop with list
print("\n=== For Loop with List ===")
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(f"I like {fruit}")

# For loop with index
print("\n=== For Loop with Index ===")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# For loop with dictionary
print("\n=== For Loop with Dictionary ===")
person = {"name": "Alice", "age": 30, "city": "Paris"}
for key, value in person.items():
    print(f"{key}: {value}")

# While loop
print("\n=== While Loop ===")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# While loop with user input simulation
print("\n=== While Loop - Countdown ===")
number = 5
while number > 0:
    print(f"{number}...")
    number -= 1
print("Blast off! 🚀")

# Nested loops
print("\n=== Nested Loops ===")
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()

# Break statement
print("\n=== Break Statement ===")
for i in range(10):
    if i == 5:
        print(f"\nBreaking at {i}")
        break
    print(i, end=" ")
print()

# Continue statement
print("\n=== Continue Statement ===")
for i in range(10):
    if i % 2 == 0:  # Skip even numbers
        continue
    print(i, end=" ")
print(" (odd numbers only)")

# Pass statement
print("\n=== Pass Statement ===")
for i in range(5):
    if i == 3:
        pass  # Do nothing, just a placeholder
    else:
        print(i, end=" ")
print()

# List comprehension (advanced loop concept)
print("\n=== List Comprehension ===")
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

even_numbers = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers: {even_numbers}")

# Loop with else clause
print("\n=== Loop with Else ===")
for i in range(5):
    print(i, end=" ")
else:
    print("\nLoop completed normally!")

# Searching in a loop
print("\n=== Searching Example ===")
numbers = [1, 3, 5, 7, 9, 11, 13]
target = 7
found = False

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        found = True
        break

if not found:
    print(f"{target} not found!")

