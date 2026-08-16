# ==========================================
# HIERARCHICAL INHERITANCE IN PYTHON
# ==========================================

# Parent class
class Animal:

    # Parent class method
    def eat(self):
        print("Animal is eating.")

    # Another parent class method
    def sleep(self):
        print("Animal is sleeping.")


# First child class
class Dog(Animal):

    # Dog's own method
    def bark(self):
        print("Dog is barking.")


# Second child class
class Cat(Animal):

    # Cat's own method
    def meow(self):
        print("Cat is meowing.")


# Create Dog object
dog = Dog()

# Dog can use parent class methods
dog.eat()
dog.sleep()

# Dog's own method
dog.bark()

print()

# Create Cat object
cat = Cat()

# Cat can use parent class methods
cat.eat()
cat.sleep()

# Cat's own method
cat.meow()
