# Print numbers from 1 to 10
for i in range(1, 11):
    print(i)
# Print even numbers from 1 to 20
for i in range(1, 21):

    # Check if number is divisible by 2
    if i % 2 == 0:
        print(i)
# Print odd numbers from 1 to 20
for i in range(1, 21):

    # Check if number is not divisible by 2
    if i % 2 != 0:
        print(i)
# Take a number from the user
num = int(input("Enter a number: "))

# Print multiplication table
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
# Store the sum
total = 0

# Loop from 1 to 10
for i in range(1, 11):
    total = total + i

# Print the sum
print("Sum =", total)
# Start with 1
i = 1

# Loop until 10
while i <= 10:
    print(i)

    # Increase number by 1
    i += 1
