
while True:
    try:
        age = int(input("Enter your age: "))
        print(age)
    except ValueError:
        print("Please enter a number")
    else:
        print("Goodbye")
        break