"""
Python Classes and Objects - Intermediate
==========================================

This script demonstrates object-oriented programming concepts in Python.
"""

# Simple class
class Dog:
    """A simple Dog class."""
    
    def __init__(self, name, breed):
        """Initialize a Dog object."""
        self.name = name
        self.breed = breed
    
    def bark(self):
        """Make the dog bark."""
        return f"{self.name} says: Woof! Woof!"
    
    def introduce(self):
        """Introduce the dog."""
        return f"Hi, I'm {self.name}, a {self.breed}."

print("=== Simple Class ===")
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.introduce())
print(my_dog.bark())

# Class with attributes and methods
class BankAccount:
    """A BankAccount class with balance management."""
    
    # Class variable (shared by all instances)
    bank_name = "Python Bank"
    
    def __init__(self, account_holder, initial_balance=0):
        """Initialize a BankAccount."""
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Deposit amount must be positive"
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdrew ${amount}. New balance: ${self.balance}"
            return "Insufficient funds"
        return "Withdrawal amount must be positive"
    
    def get_balance(self):
        """Get the current balance."""
        return f"Balance: ${self.balance}"
    
    def __str__(self):
        """String representation of the object."""
        return f"Account: {self.account_holder}, Balance: ${self.balance}"

print("\n=== BankAccount Class ===")
account = BankAccount("Alice", 1000)
print(account)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())
print(f"Bank: {BankAccount.bank_name}")

# Inheritance
class Animal:
    """Base Animal class."""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        """Make a generic animal sound."""
        return "Some generic animal sound"
    
    def introduce(self):
        """Introduce the animal."""
        return f"I'm {self.name}, a {self.species}"

class Cat(Animal):
    """Cat class inheriting from Animal."""
    
    def __init__(self, name, breed):
        super().__init__(name, "cat")
        self.breed = breed
    
    def make_sound(self):
        """Override the make_sound method."""
        return "Meow! Meow!"
    
    def purr(self):
        """Cat-specific method."""
        return f"{self.name} is purring... Purrrrr"

class Bird(Animal):
    """Bird class inheriting from Animal."""
    
    def __init__(self, name, can_fly=True):
        super().__init__(name, "bird")
        self.can_fly = can_fly
    
    def make_sound(self):
        """Override the make_sound method."""
        return "Tweet! Tweet!"
    
    def fly(self):
        """Bird-specific method."""
        if self.can_fly:
            return f"{self.name} is flying!"
        return f"{self.name} cannot fly"

print("\n=== Inheritance ===")
cat = Cat("Whiskers", "Persian")
print(cat.introduce())
print(cat.make_sound())
print(cat.purr())

bird = Bird("Tweety", can_fly=True)
print(bird.introduce())
print(bird.make_sound())
print(bird.fly())

# Encapsulation with private attributes
class Student:
    """Student class demonstrating encapsulation."""
    
    def __init__(self, name, student_id):
        self.name = name
        self.__student_id = student_id  # Private attribute
        self.__grades = []  # Private attribute
    
    def add_grade(self, grade):
        """Add a grade to the student's record."""
        if 0 <= grade <= 100:
            self.__grades.append(grade)
            return "Grade added successfully"
        return "Grade must be between 0 and 100"
    
    def get_average(self):
        """Calculate and return the average grade."""
        if self.__grades:
            return sum(self.__grades) / len(self.__grades)
        return 0
    
    def get_info(self):
        """Get student information."""
        return f"Name: {self.name}, ID: {self.__student_id}, Average: {self.get_average():.2f}"

print("\n=== Encapsulation ===")
student = Student("Bob", "S12345")
student.add_grade(85)
student.add_grade(90)
student.add_grade(78)
print(student.get_info())

# Class methods and static methods
class MathUtils:
    """Class demonstrating class methods and static methods."""
    
    PI = 3.14159
    
    @staticmethod
    def add(a, b):
        """Static method - doesn't need class or instance."""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """Static method."""
        return a * b
    
    @classmethod
    def circle_area(cls, radius):
        """Class method - has access to class variables."""
        return cls.PI * radius ** 2
    
    @classmethod
    def get_pi(cls):
        """Class method to get PI."""
        return cls.PI

print("\n=== Class Methods and Static Methods ===")
print(f"Static method: 5 + 3 = {MathUtils.add(5, 3)}")
print(f"Static method: 4 * 7 = {MathUtils.multiply(4, 7)}")
print(f"Class method: Circle area (r=5) = {MathUtils.circle_area(5):.2f}")
print(f"Class method: PI = {MathUtils.get_pi()}")

# Special methods (dunder methods)
class Book:
    """Book class demonstrating special methods."""
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """String representation for users."""
        return f"{self.title} by {self.author} ({self.pages} pages)"
    
    def __repr__(self):
        """String representation for developers."""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """Return the number of pages."""
        return self.pages
    
    def __eq__(self, other):
        """Check if two books are equal."""
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

print("\n=== Special Methods ===")
book1 = Book("Python Basics", "John Doe", 300)
book2 = Book("Python Basics", "John Doe", 350)
print(str(book1))
print(repr(book1))
print(f"Book length: {len(book1)} pages")
print(f"book1 == book2: {book1 == book2}")

