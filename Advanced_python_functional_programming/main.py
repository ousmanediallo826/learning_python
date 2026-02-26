def multiply(list):
    new_list = []
    for i in list:
        new_list.append(i * 2)
    return new_list

print(multiply([1, 2, 3]))


#map function

def multiply_by2(item):
    return item * 2

print(list(map(multiply_by2, [1, 4, 6])))


#filter function
def check_odd(item):
    return item % 2 != 0

print(list(filter(check_odd, [1, 4, 6, 7, 9, 11])))


#Zip function
first_list = [1, 3, 2, 5, 6]
second_list = [2, 4, 6, 7, 9, 11]

print(list(zip(first_list, second_list)))


#Reduce Function
from functools import reduce
list = [1, 4, 5, 76, 9, 10]
def accumulator(acc, item):
    print(acc, item)
    acc += item
    return acc

print(reduce(accumulator, list, 0))


#List Comprehension

my_list = [char for char in 'abcdef']
print(my_list)
my_list = [num for num in range(0, 100, 2)]
print(my_list)

my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]
print(my_list4)

