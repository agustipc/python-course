###
# 02 - For loops
# Allows execute a loop while iterating over a sequence
###

import os
os.system("clear")

# list
fruits = ['apple', 'banana', 'cherry', 'mango']
for fruit in fruits:
  print(fruit)

# Iterate on any iterable object
chain = 'hello'
for letter in chain:
  print(letter)

# index with enumerate()
for index, fruit in enumerate(fruits):
  print(f'{index}: {fruit}')

# change value
for index, fruit in enumerate(fruits):
  fruits[index] = fruit.upper()
print(fruits)

# range
for number in range(5):
  print(number)

# nested loops
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
for letter in letters:
  for number in numbers:
    print(f'{letter}{number}')

# break
animas = ['cat', 'dog', 'elephant', 'lion', 'tiger']
for animal in animas:
  print(animal)
  if animal == 'elephant':
    break

# continue
for animal in animas:
  if animal == 'elephant':
    continue
  print(animal)

# list comprehension
animals = ['cat', 'dog', 'elephant', 'lion', 'tiger']
animals_upper = [animal.upper() for animal in animals]
print(animals_upper)


# show pair numbers with comprehension list
pairs = [number for number in [1, 2, 3, 4, 5, 6, 7, 8] if number % 2 == 0]
print(pairs)
