print("Welcome to the online ballot, and thank you for contributing to our government.")
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to vote.")
else:
    print("You are not old enough to vote.", end=" ")
    if age == 17:
        print("You have", (18 - age), "year until you can.")
    else:
        print("You have", (18 - age), "years until you can.")