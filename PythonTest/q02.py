'''2. Escribe una función en Python llamada `divisibles_por_n` que tome una lista de números y un número `n` como parámetros, y devuelva una nueva lista que contenga solo los números de la lista original que sean divisibles por `n`.'''

listaNumeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
nuevaLista = []
def divisibles_por_n(listaNumeros, n):
    for numero in listaNumeros:
        if numero % n == 0:
            nuevaLista.append(numero)
    return(nuevaLista)
    
    
print(divisibles_por_n(listaNumeros, 3))