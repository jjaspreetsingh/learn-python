"""
Python File Handling - Intermediate
====================================

This script demonstrates reading from and writing to files in Python.
"""

import os
import json

# Writing to a file
print("=== Writing to a File ===")
file_path = "example.txt"

# Write mode (creates new file or overwrites existing)
with open(file_path, 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a Python file handling example.\n")
    file.write("Python makes file operations easy!")

print(f"Content written to {file_path}")

# Reading from a file
print("\n=== Reading from a File ===")
with open(file_path, 'r') as file:
    content = file.read()
    print("File content:")
    print(content)

# Reading line by line
print("\n=== Reading Line by Line ===")
with open(file_path, 'r') as file:
    print("Lines:")
    for line_num, line in enumerate(file, 1):
        print(f"Line {line_num}: {line.strip()}")

# Append mode
print("\n=== Appending to a File ===")
with open(file_path, 'a') as file:
    file.write("\nThis line was appended!")

with open(file_path, 'r') as file:
    print("Updated content:")
    print(file.read())

# Reading all lines into a list
print("\n=== Reading All Lines ===")
with open(file_path, 'r') as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")
    for line in lines:
        print(f"  - {line.strip()}")

# Working with JSON files
print("\n=== JSON File Operations ===")
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "coding", "traveling"]
}

json_file = "data.json"

# Write JSON data
with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)

print(f"JSON data written to {json_file}")

# Read JSON data
with open(json_file, 'r') as file:
    loaded_data = json.load(file)
    print("Loaded JSON data:")
    print(json.dumps(loaded_data, indent=2))

# File existence check
print("\n=== File Operations ===")
if os.path.exists(file_path):
    print(f"{file_path} exists")
    file_size = os.path.getsize(file_path)
    print(f"File size: {file_size} bytes")

# Working with CSV-like data
print("\n=== CSV-like Data Handling ===")
csv_data = """Name,Age,City
Alice,30,New York
Bob,25,London
Charlie,35,Tokyo"""

csv_file = "people.csv"
with open(csv_file, 'w') as file:
    file.write(csv_data)

print(f"CSV data written to {csv_file}")

# Read and parse CSV
with open(csv_file, 'r') as file:
    lines = file.readlines()
    print("CSV content:")
    for line in lines:
        fields = line.strip().split(',')
        print(f"  {fields}")

# Error handling in file operations
print("\n=== Error Handling ===")
try:
    with open("nonexistent.txt", 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found! Creating a new one...")
    with open("nonexistent.txt", 'w') as file:
        file.write("This file was created!")

# Reading file with encoding
print("\n=== File with Encoding ===")
with open("example.txt", 'r', encoding='utf-8') as file:
    content = file.read()
    print("File read with UTF-8 encoding")

# Binary file operations
print("\n=== Binary File Operations ===")
binary_data = b"Binary data example\n12345"
binary_file = "example.bin"

with open(binary_file, 'wb') as file:
    file.write(binary_data)

with open(binary_file, 'rb') as file:
    binary_content = file.read()
    print(f"Binary content: {binary_content}")

# Clean up example files
print("\n=== Cleanup ===")
example_files = ["example.txt", "data.json", "people.csv", "nonexistent.txt", "example.bin"]
for file in example_files:
    if os.path.exists(file):
        os.remove(file)
        print(f"Removed {file}")

