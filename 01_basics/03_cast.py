###
# 03 - Casting
# Casting is when you convert a variable value from one type to another.
# Python do not convert types automatically, it has a strong type system.
###

print("Converting types:")
print("100", type("100"))
print(int("100"), type(int("100")))
print("100" + str(100))

print(float("100.0"), type(float("100.0")))

print(int(3.14), type(int(3.14)))
print(int(2.51))
# Round function rounds to the nearest odd number if the number is exactly in the middle
# is for the distribution, if always rounds up or down, the distribution would be skewed
print(round(2.5))
print(round(3.5))

print(bool(3), type(bool(3)))
print(bool(0), type(bool(0)))
print(bool(-1), type(bool(-1)))

print(bool(""), type(bool("")))
print(bool("False"), type(bool("False")))
print(bool(" "), type(bool(" ")))
