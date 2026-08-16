# ==========================================
# ENCAPSULATION IN PYTHON
# ==========================================

# Create a class
class BankAccount:

    # Constructor
    def __init__(self, name, balance):
        # Public variable
        self.name = name

        # Private variable
        self.__balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid amount")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    # Method to display balance
    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.__balance)


# Create an object
account = BankAccount("Rahul", 5000)

# Access public data
print("Name:", account.name)

# Use methods to access private data
account.show_balance()

# Deposit money
account.deposit(1000)

# Withdraw money
account.withdraw(2000)

# Display updated balance
account.show_balance()
# ==========================================
# DATA ABSTRACTION IN PYTHON
# ==========================================

# Import ABC and abstractmethod
from abc import ABC, abstractmethod


# Create an abstract class
class Shape(ABC):

    # Abstract method
    @abstractmethod
    def area(self):
        pass


# Create child class
class Rectangle(Shape):

    # Constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Implement the abstract method
    def area(self):
        return self.length * self.width


# Create another child class
class Circle(Shape):

    # Constructor
    def __init__(self, radius):
        self.radius = radius

    # Implement the abstract method
    def area(self):
        return 3.14 * self.radius * self.radius


# Create objects
rectangle = Rectangle(10, 5)
circle = Circle(7)

# Call the area method
print("Rectangle Area:", rectangle.area())
print("Circle Area:", circle.area())
