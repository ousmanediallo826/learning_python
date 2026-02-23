is_old = False
is_licensed = True

if is_old:
    print("You're old enough to drive.")
else:
    print("You're not old enough to drive.")
    is_licensed = False
    if is_licensed == False:
        print("You're not licensed to drive.")


#Tenary Operator

is_friend = False
can_message = "Message is allowed" if is_friend else "Message is not allowed"
print(can_message)


#logical Operator

is_magician = True
is_expert = False
if is_magician and is_expert:
    print("You're a master magician.")
elif is_magician or not is_expert:
    print("At least you're getting there")
else:
    print("You need magic.")


#Loops

for item in "master Ousmane Diallo":
    print(item)

#counter

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count = 0
for item in my_list:
    count += item
print(count)