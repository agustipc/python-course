###
# 03 - Range
# creates a sequence of numbers
###

import os
os.system("clear")


nums = range(5) # is not a list
# it does not create a list, but it creates a range when it needed under demand
print(nums)
print(type(nums))

# starting number
nums = range(2, 5)
print(nums)

# access
nums = range(5)
for num in nums:
  print(num)

# step
nums = range(0, 10, 2)
for num in nums:
  print(num)

# negative step
nums = range(10, 0, -1)
for num in nums:
  print(num)

# to list
nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)

# repeat action
for _ in range(3):
  print('Hello')