###
# EJERCICIOS
###
import os
os.system("clear")

print('\n-------------------')
print('Ejercicio 1: El mensaje secreto')
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
mesage = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
secreto = mesage[7:14]
print(secreto)




print('\n-------------------')
print('Ejercicio 2: Intercambio de posiciones')
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
numbers = [10, 20, 30, 40, 50]
firstNumber = numbers[0]
lastNumber = numbers[-1]
numbers[0] = lastNumber
numbers[-1] = firstNumber
print(numbers)




print('\n-------------------')
print('Ejercicio 3: El sándwich de listas')
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
sandwich = pan + ingredientes + pan_abajo
print(sandwich)




print('\n-------------------')
print('Ejercicio 4: Duplicando la lista')
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
lista = [1, 2, 3]
newList = lista + lista
print(newList)




print('\n-------------------')
print('Ejercicio 5: Extrayendo el centro')
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30
lista = [10, 20, 30, 40, 50]
center = lista[len(lista)//2]
print(center)




print('\n-------------------')
print('Ejercicio 6: Reversa parcial')
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
lista = [1, 2, 3, 4, 5, 6]
firstHalf = lista[:len(lista)//2]
secondHalf = lista[len(lista)//2:]
newList = firstHalf[::-1] + secondHalf
print(newList)