age = 20

if age >= 18:
    print("You are an adult")

age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")

marks = 75

if marks >= 90:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 40:
    print("C")
else:
    print("Fail")

for i in range(5):
    print(i)

i = 1

while i <= 5:
    print(i)
    i += 1

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)

for i in range(5):
    if i == 2:
        pass
    print(i)
