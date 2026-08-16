# ==========================================
# FILE HANDLING IN PYTHON
# ==========================================

# Open a file in write mode
file = open("student.txt", "w")

# Write data into the file
file.write("Name: Rahul\n")
file.write("Age: 20\n")
file.write("Course: Python\n")

# Close the file
file.close()

print("Data written successfully.")


# ------------------------------------------
# Reading the file
# ------------------------------------------

# Open the file in read mode
file = open("student.txt", "r")

# Read all data
data = file.read()

# Display the data
print(data)

# Close the file
file.close()
# ==========================================
# POLYMORPHISM IN PYTHON
# ==========================================

# Parent class
class Animal:

    # Common method
    def sound(self):
        print("Animal makes a sound")


# Child class 1
class Dog(Animal):

    # Override the sound method
    def sound(self):
        print("Dog says: Woof Woof")


# Child class 2
class Cat(Animal):

    # Override the sound method
    def sound(self):
        print("Cat says: Meow")


# Create objects
dog = Dog()
cat = Cat()

# Same method name
# But different output
dog.sound()
cat.sound()
# Parent class
class Vehicle:

    def start(self):
        print("Vehicle is starting")


# Car class
class Car(Vehicle):

    def start(self):
        print("Car is starting")


# Bike class
class Bike(Vehicle):

    def start(self):
        print("Bike is starting")


# Common function
def start_vehicle(vehicle):
    # Call the start method
    vehicle.start()


# Create objects
car = Car()
bike = Bike()

# Same function works with different objects
start_vehicle(car)
start_vehicle(bike)
