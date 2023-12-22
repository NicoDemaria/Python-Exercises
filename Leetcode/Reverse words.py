

def reverse_words(text):
    a = []
    for i in text.split(' '):
        a.append(i[::-1])
    return ' '.join(a)




print (reverse_words('double  spaces'))
# "secaps  elbuod"


# "elbuod  secaps"