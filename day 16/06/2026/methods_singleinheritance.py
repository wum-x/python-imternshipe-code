# ==========================================
# SINGLE INHERITANCE IN PYTHON
# ==========================================

# Parent class
class Animal:

    # Parent class method
    def eat(self):
        print("Animal is eating.")

    # Another parent class method
    def sleep(self):
        print("Animal is sleeping.")


# Child class inherits from Animal
class Dog(Animal):

    # Child class method
    def bark(self):
        print("Dog is barking.")


# Create an object of the child class
dog = Dog()

# Calling parent class method
dog.eat()

# Calling another parent class method
dog.sleep()

# Calling child class method
dog.bark()
