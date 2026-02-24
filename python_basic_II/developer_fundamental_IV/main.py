#find duplicates from a list


my_list =  ["a", "b", "c", "b", "d", "e", "n", "n"]
duplicates = []
for item in my_list:
    if my_list.count(item) > 1:
        duplicates.append(item)
print(duplicates)


#function in pyhton

def say_hello(name, emoji):
    print(f"Hello {name} {emoji}")
say_hello("Ousmane", "🥰")


def add(num1, num2):
    return num1 + num2

add(1, 2)



def highest_even(my_list):
    return max(my_list)

print(highest_even(my_list = [1,2,3,4,5,6,10,22]))