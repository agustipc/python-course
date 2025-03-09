###
# 04 - Listas Métodos
# Most important methods to work with lists
###


import os
os.system('clear')


print('-------------------')
print('Add items to a list')

list1 = [5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1.append(11)
print(list1)


# insert a value in a specific position by the index
list1.insert(0, 0)
print(list1)

# add elements to the end of a list
list1.extend([12, 13, 14])
print(list1)


print('\n-------------------')
print('remove items from a list')

# remove the first appearance of a value
list1.remove(5)
print(list1)

# remove the last item
popped_item = list1.pop()
print(list1)
print(popped_item)

# remove an item by index
list1.pop(0)
print(list1)

# remove a range of elements
del list1[1 : 3]
print(list1)

# remove all items
list1.clear()
print(list1)


print('\n-------------------')
print('sort items from a list')

list2 = [5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# modify the list
list2.sort()
print(list2)

list2 = [5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# return a sorted list
sorted_list = sorted(list2)
print(list2)
print(sorted_list)

fruits = ['banana', 'apple', 'orange', 'grape']
fruits.sort()
print(fruits)

fruits_uppercase = ['banana', 'apple', 'Orange', 'Grape']
fruits_uppercase.sort()
print(fruits_uppercase)

fruits_uppercase.sort(key=str.lower)
print(fruits_uppercase)


fruits = ['banana', 'apple', 'orange', 'grape', 'apple', 'grape']
print(len(fruits))
print(fruits.count('apple'))
print('apple' in fruits)


