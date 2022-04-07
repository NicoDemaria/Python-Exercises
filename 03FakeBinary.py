# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

def fake_bin(x):
    result = ""
    for num in x:
        if int(num) < 5:
            result += "0"
        else:
            result += "1"
    return result


print(fake_bin("45385593107843568"))
