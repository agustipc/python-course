###
# 04 - Functions
# A function is a block of code, reusables, which only runs when it is called.
###


import os
os.system("clear")

""" Definition of a function
def name_of_function(parameter1, parameter2, ...):
  # docsting
  # fuction body
  return return_value
"""

# function to print something
def say_hello():
  print("Hello")
# call the function
say_hello()

# function with args
def greet(name: str):
  print(f"Hello {name}")
# call the function
greet("John")
greet('Jane Smith')

# function with multiple args
def sum(a: float, b: float):
  return a + b
# call the function
result = sum(2, 3)
print(result)

# document the function with docstring
def greetings(name: str):
  """
  This function greets to the person passed in as a parameter
  """
  print(f"Hello {name}")
# call the function
greetings("John")
print(greetings.__doc__)

# function with default value
def greet2(name: str = "John"):
  print(f"Hello {name}")
# call the function
greet2()
greet2("Jane")


# arguments with key
def greet3(name: str, age: int):
  print(f"Hello {name}, you are {age} years old")
# call the function
greet3(age=30, name="John")

# function with variable number of arguments
def greet4(*names: str):
  for name in names:
    print(f"Hello {name}")
# call the function
greet4("John", "Jane", "Doe")

def sum2(*args: float):
  total = 0
  for num in args:
    total += num
  return total
# call the function
result = sum2(1, 2, 3, 4, 5)
print(result)

# function with variable number of keyword arguments
def greet5(**kwargs: str | int):
  for key, value in kwargs.items():
    print(f"{key}: {value}")
# call the function
greet5(name="John", age=30, city="New York")