# Operator Precedance

print((5 + 4) * 10 / 2) #45

print(((5 + 4) * 10) / 2) # 45

print((5 + 4) * (10 / 2)) # 45

print(5 + (4 * 10) / 2) # 25

print(5 + 4 * 10 // 2) # 25

print(bin(10))



# Variables in python

user_iq = 190
user_name = "Ousmane Diallo"
print(user_name, "has",  user_iq, "iq.")


# String Concatenation

print("hello" + " Ousmane Diallo")

#python methos & functions

print(len("Ousmane Diallo"))


#type conversion

birth_year = input("Please enter your birth year: ")
dob = 2026 - int(birth_year)
print(f"your birth year is {dob}")