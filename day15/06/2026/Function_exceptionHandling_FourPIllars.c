# ==========================================================
# 1. FUNCTION
# ==========================================================

# Creating a function
def add(a, b):
    # Add two numbers
    result = a + b

    # Return the result
    return result


# Calling the function
answer = add(10, 20)

# Display result
print("Addition =", answer)


# ==========================================================
# 2. EXCEPTION HANDLING
# ==========================================================

try:
    # Take two numbers from the user
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    # Perform division
    result = a / b

    print("Result =", result)

except ValueError:
    # Handles invalid input
    print("Please enter numbers only.")

except ZeroDivisionError:
    # Handles division by zero
    print("Cannot divide by zero.")

finally:
    # This always executes
    print("Program completed.")


# ==========================================================
# 3. ENCAPSULATION
# ==========================================================

class BankAccount:

    def __init__(self, balance):
        # Private variable
        self.__balance = balance

    # Method to deposit money
    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited:", amount)

    # Method to display balance
    def show_balance(self):
        print("Balance:", self.__balance)


# Create object
account = BankAccount(5000)

# Access data through methods
account.deposit(1000)
account.show_balance()


# ==========================================================
# 4. INHERITANCE
# ==========================================================

# Parent class
class Animal:

    def eat(self):
        print("Animal is eating.")


# Child class
class Dog(Animal):

    def bark(self):
        print("Dog is barking.")


# Create object of child class
dog = Dog()

# Calling inherited method
dog.eat()

# Calling child class method
dog.bark()


# ==========================================================
# 5. POLYMORPHISM
# ==========================================================

# Parent class
class Vehicle:

    def start(self):
        print("Vehicle is starting.")


# Child class 1
class Car(Vehicle):

    # Override start method
    def start(self):
        print("Car is starting.")


# Child class 2
class Bike(Vehicle):

    # Override start method
    def start(self):
        print("Bike is starting.")


# Create objects
car = Car()
bike = Bike()

# Same method, different behavior
car.start()
bike.start()


# ==========================================================
# 6. ABSTRACTION
# ==========================================================

from abc import ABC, abstractmethod


# Abstract class
class Shape(ABC):

    # Abstract method
    @abstractmethod
    def area(self):
        pass


# Child class
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Implement abstract method
    def area(self):
        return self.length * self.width


# Create object
rectangle = Rectangle(10, 5)

# Calculate area
print("Rectangle Area =", rectangle.area())
