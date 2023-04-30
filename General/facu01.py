'''debera ingresar dos numeros e indicar cuantas vueltas se tienen que dar para llegar a 100'''


num1 = int(input("Ingrese el primer numero: "))
contador = 0


while num1 < 100:
    num1 += 1
    contador += 1
    
print('Para el primer numero',"Se tuvieron que dar", contador, "vueltas para llegar a 100")

num2 = int(input("Ingrese el primer numero: "))
contador2 = 0


while num2 < 100:
    num2 += 1
    contador2 += 1
    
print('Para el primer numero',"Se tuvieron que dar", contador2, "vueltas para llegar a 100")