# Python Cheat Sheets

Quick reference guides for common Python operations.

## Variables and Data Types

```python
# Numbers
x = 10          # Integer
y = 3.14        # Float
z = 2 + 3j      # Complex

# Strings
name = "Python"
message = 'Hello'

# Boolean
is_true = True
is_false = False

# Collections
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_dict = {'key': 'value'}
my_set = {1, 2, 3}
```

## String Operations

```python
s = "Hello, World!"

s.upper()           # "HELLO, WORLD!"
s.lower()           # "hello, world!"
s.strip()           # Remove whitespace
s.split(',')        # ['Hello', ' World!']
s.replace('H', 'J') # "Jello, World!"
len(s)              # 13
```

## List Operations

```python
my_list = [1, 2, 3]

my_list.append(4)      # [1, 2, 3, 4]
my_list.insert(0, 0)   # [0, 1, 2, 3, 4]
my_list.remove(2)      # [0, 1, 3, 4]
my_list.pop()          # Returns 4, list: [0, 1, 3]
my_list.index(1)       # 1
my_list.count(3)       # 1
len(my_list)           # 3
```

## Dictionary Operations

```python
my_dict = {'name': 'Alice', 'age': 30}

my_dict['city'] = 'NYC'        # Add key-value
my_dict.get('name')            # 'Alice'
my_dict.keys()                 # dict_keys(['name', 'age', 'city'])
my_dict.values()               # dict_values(['Alice', 30, 'NYC'])
my_dict.items()                # dict_items([('name', 'Alice'), ...])
'name' in my_dict              # True
del my_dict['age']             # Remove key
```

## Control Flow

```python
# If-elif-else
if condition:
    pass
elif other_condition:
    pass
else:
    pass

# For loop
for item in iterable:
    pass

# While loop
while condition:
    pass

# Break and continue
for i in range(10):
    if i == 5:
        break       # Exit loop
    if i % 2 == 0:
        continue    # Skip to next iteration
```

## Functions

```python
# Simple function
def my_function():
    return "Hello"

# Function with parameters
def greet(name, age=18):
    return f"Hi {name}, you are {age}"

# Lambda function
square = lambda x: x ** 2

# *args and **kwargs
def func(*args, **kwargs):
    pass
```

## File Operations

```python
# Read file
with open('file.txt', 'r') as f:
    content = f.read()

# Write file
with open('file.txt', 'w') as f:
    f.write("Hello")

# Append to file
with open('file.txt', 'a') as f:
    f.write("World")

# Read line by line
with open('file.txt', 'r') as f:
    for line in f:
        print(line)
```

## List Comprehensions

```python
# Basic
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# Nested
matrix = [[i*j for j in range(3)] for i in range(3)]
```

## Error Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Error: {e}")
else:
    print("No errors")
finally:
    print("Always executed")
```

## Classes

```python
class MyClass:
    class_var = "shared"
    
    def __init__(self, value):
        self.instance_var = value
    
    def method(self):
        return self.instance_var
    
    @staticmethod
    def static_method():
        return "static"
    
    @classmethod
    def class_method(cls):
        return cls.class_var
```

## Useful Built-in Functions

```python
# Type and conversion
type(x)
int('10')
str(10)
float('3.14')
list(range(5))

# Common functions
len([1, 2, 3])
max(1, 2, 3)
min(1, 2, 3)
sum([1, 2, 3])
sorted([3, 1, 2])
reversed([1, 2, 3])

# Enumerate and zip
for i, item in enumerate(['a', 'b', 'c']):
    print(i, item)

for a, b in zip([1, 2], ['a', 'b']):
    print(a, b)
```

