# Creating a list
numbers = [10, 20, 30, 40, 50]

# Print the complete list
print("List:", numbers)

# Access the first element
print("First element:", numbers[0])

# Access the last element
print("Last element:", numbers[-1])

# Add an element
numbers.append(60)

# Change an element
numbers[1] = 25

# Remove an element
numbers.remove(40)

# Print updated list
print("Updated List:", numbers)
# Creating a nested list
students = [
    ["Rahul", 20, "Python"],
    ["Amit", 21, "Java"],
    ["Priya", 19, "C"]
]

# Print the complete nested list
print("Students:", students)

# Access first student's details
print("First Student:", students[0])

# Access first student's name
print("Name:", students[0][0])

# Access second student's age
print("Age:", students[1][1])

# Access third student's course
print("Course:", students[2][2])
# Creating a nested list
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Outer loop
for row in numbers:

    # Inner loop
    for number in row:
        print(number, end=" ")

    # Move to the next line
    print()
# Creating a nested list
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Outer loop
for row in numbers:

    # Inner loop
    for number in row:
        print(number, end=" ")

    # Move to the next line
    print()
