###
# 02 - booleans
# logic values : True, False
###

# comparison operators
print("5 > 3:", 5 > 3)      # True
print("5 < 3:", 5 < 3)      # False
print("5 == 5", 5 == 5)     # True
print("5 != 3", 5 != 3)     # type: ignore # True
print("5 >= 5", 5 >= 5)     # True
print("5 <= 3", 5 <= 3)     # False


# lexico-graphic comparison
print("apple < rat", 'apple' < 'rat')       # True  compares the first letter of each string, if both are the same, compares the next letter
print("apple == Apple", 'apple' == 'Apple')   # type: ignore # False case sensitive