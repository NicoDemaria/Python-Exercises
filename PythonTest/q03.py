'''Escribe un código en Python que lea el contenido de un archivo de texto llamado "datos.txt" y cuente la cantidad de líneas que contiene.'''

with open("lista_compras.txt") as archivo:
    total_lines = sum(1 for line in archivo)
    
print(total_lines)
