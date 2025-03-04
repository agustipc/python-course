"""
comments
"""

print('int:')
print(10, type(10))
print(-1, type(-1))
print(123554322, type(123554322))
# ints can be as big as you want
print(73678293846519382474716384984848488 + 1)


print('\nfloat:')
print(10.0, type(10.0))
print(-1.0, type(-1.0))
print(123554322.0, type(123554322.0))
print(1e3, type(1e3))


print('\ncomplex:')
print(10 + 0j, type(10 + 0j))


print('\nstr:')
print('Hello', type('Hello'))
print('', type(''))
print('123', type('123'))
print("""
      Multiline
""")


print('\nbool:')
print(True, type(True))
print(False, type(False))
print(1 == 1, type(1 == 1))



print('\nNone:')
print(None, type(None))