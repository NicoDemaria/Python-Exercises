'''This Kata is intended as a small challenge for my students

All Star Code Challenge #18

Create a function that accepts 2 string arguments and returns an integer of the count of occurrences the 2nd argument is found in the first one.
If no occurrences can be found, a count of 0 should be returned.
https://www.codewars.com/kata/5865918c6b569962950002a1/train/python
'''


def str_count(strng, letter):
    count = 0
    for i in strng:
        if i == letter:
            count += 1
    return count


print(str_count("Helloooo", "o"))
