###
# 04 - Variables
# Variables are used to store data values.
# python is a strong and dynamic typed language
###

my_name = 'Agustí'

print(my_name)

age = 25
print(age)

age = 28
print(age)



# Dynamic typing
# type of data is determined at runtime

name =  "agusti"
print(type(name))

name = 28
print(type(name))



# Strong typing
print(f"Hello {my_name} you are {age} years old")


# Do not recomended
name, age, city = "Agustí", 25, "Barcelona"
print(name, age, city)


# Naming conventions
#snakecase
my_name = "Agustí"
# Uppercase for consts but is not real const
MY_NAME = "Agustí"



#  Types annotation
is_user_logged: bool = True
# you can still change the type of the variable is_user_logged = 1
# but if you change typecheck in editor config to strinct it will warn you