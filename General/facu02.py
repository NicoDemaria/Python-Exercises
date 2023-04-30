'''
ingresar un monto y cantidad de cuotas,
cuotas < 3 se aumenta un 10% al monto
cuotas < 7 se aumenta un 30% al monto
cuotas llegana  12  se aumenta un 20% al monto
'''

monto = int(input("Ingrese el monto: "))
cuotas = int(input('Ingrese la cantidad de cuotas: '))

if cuotas < 3:
    monto = monto * 1.1
elif cuotas < 7:
    monto = monto* 1.3
elif cuotas <= 12:
    monto = monto * 1.2