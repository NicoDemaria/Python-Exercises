'''
Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python'''


def get_sum(a, b):
    c = 0

    if a == b:
        return b
    for i in range(min(a, b), max(a, b)+1):
        c += i
    return c
