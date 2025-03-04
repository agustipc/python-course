###
# 03 - Lists
###

import os
os.system("clear")

list = []
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [1, 'a', 2, 'b', 3, 'c', True, False] # type: ignore
list_of_lists = [[1, 2, 3], ['a', 'b', 'c'], [True, False, True]] # type: ignore
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Accessing elements
print(list1[0])
print(matrix[1][len(matrix) - 1])
print(list2[-1])

# slicing
print(list2[2:4])
print(list1[:3])
print(list1[2:])
print(list1[::2])
print(list1[::-1])


# Modifying lists
list1[0] = 10
print(list1)

list1 = list1 + [6, 7, 8]
print(list1)

list1 += [9, 10]
print(list1)

list1.append(11)
print(list1)