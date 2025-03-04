###
# 01 - Conditional Statements
# if, elif, else
###

import os
os.system("clear")

# simple contidianal statement

age = 14

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a minor")



# multiple conditinal

age = 12
has_id = True

if age >= 18 and has_id:
    print("You can enter the club")
else:
    print("You can't enter the club")


# or operator

cash = 1
money_in_card = 100

if cash >= 21.99 or money_in_card >= 21.99:
    print("You can pay the bill")
else:
    print("You can't pay the bill")


# not operator

is_weekend = False

if not is_weekend:
    print('You have to work')
else: 
    print('You can sleep all day')


# nest conditionals

age = 22
has_money = False

if age >= 18:
    if has_money:
        print("You can buy a beer")
    else:
        print("You can't buy a beer, you have no money")
else:
    print("You can't buy a beer, you are a minor")


# booleans
number = 5
if number:
    print('The number is not zero')

number = 0
if not number:
    print('The number is zero')

# texts
name = 'John'
if name:
    print('The name is not empty')

name = ''
if not name:
    print('The name is empty')


# ternary operator
# [code if the condition is true] if [condition] else [code if the condition is false]
age = 14
print('You are an adult' if age >= 18 else 'You are a minor')