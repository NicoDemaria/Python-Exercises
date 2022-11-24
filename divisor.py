'''
Count the number of divisors of a positive integer n.

Random tests go up to n = 500000.

Examples (input --> output)


'''


def divisors(n):
    count = 0

    for number in range(1, n + 1):
        if n % number == 0:
            count += 1

# correcto


def divisors(n):
    i = 1
    result = 0
    while i <= n:
        if n % i == 0:
            result += 1
        i += 1
    return result
