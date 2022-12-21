'''I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:

humanYears >= 1
humanYears are whole numbers only
Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that
Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that
'''

# 4


def human_years_cat_years_dog_years(human_years):
    catYear = 0
    dogYear = 0
    for i in range(human_years):
        if human_years == 1:
            catYear = 15
            dogYear = 15
        elif human_years == 2:
            catYear = 24
            dogYear = 24
        else:
            catYear = 4 * (human_years - 2) + 24
            dogYear = 5 * (human_years - 2) + 24

    return [human_years, catYear, dogYear]


cat, dog = human_years_cat_years_dog_years(3)
print(cat, dog)
