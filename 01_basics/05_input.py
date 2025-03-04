###
# 05 - User inputs (input())
# input() is a function that allows you to get user input from the console.
###

import os
os.system("clear")

print("Hello, what's your name?")
name = input()
age = input(f"Hello, {name}, what's your age?\n")

print(f"In 10 years you will be {int(age) + 10} years old")


# Obtain multiple values

country, city = input("Enter your country and city separated by a comma: ").split(",")
print(f"Country: {country}, City: {city}")
