# Exercise 1
import random

my_list = []
length = int(input("input the length of list:\t"))
for i in range(length):
    my_list.append(random.randint(0, 50))
print(my_list)


def sum_of_numbers(my_list):
    if len(my_list) == 0:
        return 0
    else:
        return my_list[0] + sum_of_numbers(my_list[1:])


print(sum_of_numbers(my_list))


# Exercise 2

def factorial(num):
    if num == 1:
        return 1
    elif num == 0:
        print("the factorial is : 1")
    elif num < 0:
        return
    else:
        return num * factorial(num - 1)


num = int(input("input the number\t"))
print(factorial(num))


# Exercise 4

def hamonic(n):
    if n < 2:
        return 1
    elif n < 0:
        print("number must be positive")
    else:
        return 1 / n + hamonic(1 / (n - 1))


n = float(input("please input the number:\t"))
print(hamonic(n))
