a = [1,3,5,7,9,10,11,12,13,14]
b = [2,4,6,8,9,11,12,13]

commonNumbers = []
for numA in a:
    for numB in b:
        if numA == numB:
            commonNumbers.append(numA)
        
        
print(commonNumbers)   