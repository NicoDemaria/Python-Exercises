'''1. Escribe un código en Python que tome una lista de números y devuelva una nueva lista que contenga solo los números pares.''' 

listaNumeros = [1,2,3,4,5,6,7,8,9,10]
listaPares = []

for numero in listaNumeros:
    if numero  % 2 == 0:
        listaPares.append(numero)
        
        
print(listaPares)