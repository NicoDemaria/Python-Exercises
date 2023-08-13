'''5. Escribe un código en Python que maneje una excepción de división por cero. El código debe solicitar al usuario que ingrese dos números y realizar la división. Si el denominador es cero, se debe capturar la excepción y mostrar un mensaje de error.
'''



n1 = int(input('Ingrese el primer numero'))
n2 = int(input('Ingrese el segundo numero'))

try:
    num = n1/n2
    print(num)
except:
    print('No se puede dividir con deniminador 0')

