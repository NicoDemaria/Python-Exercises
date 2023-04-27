import math
numeros = [18,22,25,48,50,67,85]

media = sum(numeros)/len(numeros)

varianza = 0


for num in numeros:
    varianza += ((num - media)**2)/len(numeros)
    
print(varianza)


standard_deviation = math.sqrt(varianza)

print(standard_deviation)