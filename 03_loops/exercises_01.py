###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
counter = 10
while counter > 0:
  print(counter)
  counter -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
counter = 1
total = 0
while counter <= 20:
  if counter % 2 == 0:
    total += counter
  counter += 1
print(total)

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")
number = -1
while number < 0:
  try:
    number = int(input('Enter a positive number: '))
    if number < 0:
      print('The number must be positive')
    else:
      factorial = 1
      while number > 0:
        factorial *= number
        number -= 1
      print(f'The factorial is {factorial}')
  except:
    print('The input should be a number')


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")
password = ''
while len(password) < 8:
  password = input('Enter a password with at least 8 characters: ')
  if len(password) < 8:
    print('The password must have at least 8 characters')
print('Valid password')

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

number = input('Enter a number: ')
multiplyer = 1

while multiplyer <= 10:
  print(f'{number} x {multiplyer} = {int(number) * multiplyer}')
  multiplyer += 1


# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

number = int(input('enter a number: '))

while number > 1:
  i= 2
  is_prime = True

  while i * i <= number:
    if number % i == 0:
      is_prime = False
      break
    i += 1
  if is_prime:
    print(number)
    
  number -= 1