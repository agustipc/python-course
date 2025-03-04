###
# EJERCICIOS
###
import os
os.system("clear")

print('\n-------------------')
print('Ejercicio 1: Determinar el mayor de dos números')
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

num1 = int(input('introduce el primer numero: \n'))
num2 = int(input('introduce el segundo numero: \n'))
if num1 > num2:
    print(f'{num1} es mayor que {num2}')
elif num1 < num2:
    print(f'{num2} es mayor que {num1}')
else:
    print('los numeros son iguales')




print('\n-------------------')
print('Ejercicio 2: Calculadora simple')
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

num1 = int(input('introduce el primer numero: \n'))
num2 = int(input('introduce el segundo numero: \n'))
operacion = input('introduce la operacion a realizar (+, - , *, /): \n')
if operacion == '+':
    print(f'la suma de {num1} y {num2} es {num1 + num2}')
elif operacion == '-':
    print(f'la resta de {num1} y {num2} es {num1 - num2}')
elif operacion == '*':
    print(f'la multiplicacion de {num1} y {num2} es {num1 * num2}')
elif operacion == '/':
    if num2 == 0:
        print('no se puede dividir entre 0')
    else:
        print(f'la division de {num1} y {num2} es {num1 / num2}')
else:
    print('operacion no valida')




print('\n-------------------')
print('Ejercicio 3: Año bisiesto')
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
year = int(input('introduce el año: \n'))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f'{year} es un año bisiesto')
else:
    print(f'{year} no es un año bisiesto')


print('\n-------------------')
print('Ejercicio 4: Categorizar edades')
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

year = int(input('introduce una edad: \n'))
if year >= 0 and year <= 2:
    print('bebe')
elif year >= 3 and year <= 12:
    print('niño')
elif year >= 13 and year <= 17:
    print('adolescente')
elif year >= 18 and year <= 64:
    print('adulto')
else:
    print('adulto mayor')