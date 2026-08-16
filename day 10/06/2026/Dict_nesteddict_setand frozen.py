# Creating a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

# Printing the dictionary
print(student)

# Accessing values using keys
print("Name:", student["name"])
print("Age:", student["age"])

# Adding a new key-value pair
student["city"] = "Pune"

# Updating a value
student["age"] = 21

# Printing updated dictionary
print(student)
# Creating a nested dictionary
students = {
    "student1": {
        "name": "Rahul",
        "age": 20,
        "course": "Python"
    },

    "student2": {
        "name": "Amit",
        "age": 21,
        "course": "Java"
    }
}

# Print complete dictionary
print(students)

# Access student1 name
print(students["student1"]["name"])

# Access student2 course
print(students["student2"]["course"])
# Creating a set
numbers = {10, 20, 30, 40, 20}

# Duplicate 20 is automatically removed
print(numbers)

# Add an element
numbers.add(50)

# Remove an element
numbers.remove(30)

# Print updated set
print(numbers)
# Creating two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union
print("Union:", A | B)

# Intersection
print("Intersection:", A & B)

# Difference
print("Difference:", A - B)
# Creating a frozenset
numbers = frozenset([10, 20, 30, 40])

# Print frozenset
print(numbers)

# Check whether an element exists
if 20 in numbers:
    print("20 is present")

# Find the number of elements
print("Length:", len(numbers))
# Creating two frozensets
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# Union
print("Union:", A | B)

# Intersection
print("Intersection:", A & B)

# Difference
print("Difference:", A - B)
