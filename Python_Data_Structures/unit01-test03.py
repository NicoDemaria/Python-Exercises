"""input manatees: a list of "manatees", where one manatee is represented by a dictionary
a single manatee has properties like "name", "age", et cetera
n = the number of elements in "manatees"
m = the number of properties per "manatee" (i.e. the number of keys in a manatee dictionary)"""

manatees = [
    {'name': 'Manatí 1', 'age': 10},
    {'name': 'Manatí 2', 'age': 15},
    {'name': 'Manatí 3', 'age': 20}
]
import time
inicio = time.time()

# Código a medir
def example4(manatees):
    oldest_manatee = "No manatees here!"
    for manatee1 in manatees:
        for manatee2 in manatees:
            if manatee1['age'] < manatee2['age']:
                oldest_manatee = manatee2['name']
            else:
                oldest_manatee = manatee1['name']
    print (oldest_manatee)
    
# -------------
example4(manatees)

fin = time.time()
print(fin-inicio)

def example1(manatees):
    for manatee in manatees:
        print (manatee['name'])

def example2(manatees):
    print (manatees[0]['name'])
    print (manatees[0]['age'])

def example3(manatees):
    for manatee in manatees:
        for manatee_property in manatee:
            print (manatee_property), ": ", manatee[manatee_property]

def example4(manatees):
    oldest_manatee = "No manatees here!"
    for manatee1 in manatees:
        for manatee2 in manatees:
            if manatee1['age'] < manatee2['age']:
                oldest_manatee = manatee2['name']
            else:
                oldest_manatee = manatee1['name']
    print (oldest_manatee)
    
