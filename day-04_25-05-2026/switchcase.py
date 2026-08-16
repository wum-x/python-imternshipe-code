# Switch Case Example in Python

# Take a choice from the user
choice = int(input("Enter your choice (1-3): "))

# Match the choice
match choice:

    # If choice is 1
    case 1:
        print("You selected One")

    # If choice is 2
    case 2:
        print("You selected Two")

    # If choice is 3
    case 3:
        print("You selected Three")

    # If no case matches
    case _:
        print("Invalid choice")
