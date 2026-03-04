import random

def guessing_game():
    user_attempt = 10
    try:
        while True:

            computer = random.randint(1, 10)
            user_input = int(input("Enter a number: "))
            if computer > user_input:
                print("Your guess is to low")

            elif computer < user_input:
                print("Your guess is to high")
            elif computer == user_input:
                print("You guessed it correctly")
                break

            else:
                print("Please enter a number between 1 and 10")
                continue
            user_attempt -= 1
            if user_attempt == 0:
                break
    except ValueError as err:
        print("Please enter a positive integer")


guessing_game()