###
# 01 - Loop While
# loops until a condition is true
###


import os
os.system("clear")

counter = 0
while counter < 5:
  print(counter)
  counter += 1


# break to stop loop
counter = 0
while counter <= 100:
  print(counter)
  counter += 1
  if counter % 10 == 0:
    break



print('\n----------')
print('countinuous loop')
counter = 0

while counter < 10:
  counter += 1

  if counter % 2 == 0:
    continue

  print(counter)


print('\n----------')
print('while with else')

counter = 0
while counter < 5:
  print(counter)
  counter += 1
else:
  print('Loop finished')


print('\n----------')
print('ask the user a number that has to be positive')

number = -1
while number < 0:
  try:
    number = int(input('Enter a positive number: '))
    if number < 0:
      print('The number must be positive')
  except:
    print('The input should be a number')

print(f'the number is {number}')