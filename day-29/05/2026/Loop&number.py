# Take a number from the user
num = int(input("Enter a number: "))

# Assume the number is prime
is_prime = True

# Check divisibility
if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

# Display result
if is_prime:
    print("Prime number")
else:
    print("Not a prime number")

# Take a number from the user
num = int(input("Enter a number: "))

# Reverse the number
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

# Print reversed number
print("Reverse =", reverse)

# Take a number from the user
num = int(input("Enter a number: "))

# Start factorial with 1
fact = 1

# Calculate factorial
for i in range(1, num + 1):
    fact = fact * i

# Print result
print("Factorial =", fact)
