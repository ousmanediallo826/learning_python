# # Creating my Own Object
#
# class PlayerCharacter:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def run(self):
#         print("run", self.name)
#
#
# player1 = PlayerCharacter("Ousmane", 30)
# player2 = PlayerCharacter("Alhassane", 44)
# print(player1.name, player1.age)
# print(player2.name, player2.age)
#
#
# #Given the below class:
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# # 1 Instantiate the Cat object with 3 cats
#
# cat1 = Cat("Mammal", 20)
# cat2 = Cat("Mammal", 40)
# cat3 = Cat("Mammal", 50)
#
# # 2 Create a function that finds the oldest cat
# def is_oldest_cat(*args):
#         return max(args)
#
# print(f'Oldest Cat is {is_oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')
#
#
#
#
#
# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2


class User:
    def is_logged_in(self):
        print("You're logged in.")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attck(self):
        print(f"Attacking with power of {self.power}.")

class Archer(User):
    def __init__(self, name, nums_arrows):
        self.name = name
        self.nums_arrows = nums_arrows

    def attck(self):
        print(f"Attacking with nums of arrows of {self.nums_arrows}.")


Wizard1 = Wizard("Merlin", 50)
Archer1 = Archer("Ousmane", 500)
print(Wizard1.attck())
print(Archer1.attck())