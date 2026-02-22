#password Checkr

user_name = input("Please enter your name: ")
password = input("Please enter your password: ")

encrypted_password = ("*" * len(password))

print(f"Hi, {user_name}, your password is {encrypted_password} ans it is {len(password)} digits long.")