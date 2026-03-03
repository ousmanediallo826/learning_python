# import random
#
# print(random.random())
# print(random.choifce([1,2,3,4,5,6,7,8,9,10]))

import random




user_attempt = 10
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