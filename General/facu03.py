''''
Ingresar dos valores con limite en 100,
el primer aumenta de 5 
y el segudno aumenta de a 7
mostrar el mayor

'''



num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

while num1 < 100 and num2 < 100:
    num1 += 5
    num2 += 7

if num1 > num2:
    print("El numero mayor es", num1)
else:
    print("El numero mayor es", num2)