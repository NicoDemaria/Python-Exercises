'''
Input parameters
pandas.DataFrame object
sequence
Task
Your function must return a new pandas.DataFrame object with same data than the original input but now its column names are the elements of the sequence. You must not modify the original input.

The number of columns of the input will always be equal to the size of the sequence.
https://www.codewars.com/kata/5e60cdcd01712200335bd676/train/python'''


import pandas as pd


def rename_columns(df, names):

    return pd.DataFrame(data=df.values, columns=names)


def rename_columns(df, names):
    return pd.DataFrame(data=df.values, columns=names)
