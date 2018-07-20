# 1. Using the random module and the range method, generate a list of 20 random numbers between 0 and 49.

import random

random_numbers = [] #empty list
for n in range(20): # "generate 20 numbers starting from 0"
    random_numbers.append(random.randint(0, 49)) # "return a random integer from 0-40"

print("Twenty #s Between 0 and 40 = ", random_numbers)


# 2. With the resulting list, use a list comprehension to build a new list that contains each number squared. For example, if the original list is [2, 5], the final list will be [4, 25].

# [ ] indicates a list
new_set = [number*2 for number in random_numbers] # loop through random_numbers

print("New Set Squared = ", new_set)