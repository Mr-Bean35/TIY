# File : 10-1, 10-2.py
# Date : 4/18/2022
# Author : Benjamin Hensley Jr.

import sys, time, math


def next():
    print(f'\n')


with open('learning_python (10-1).txt') as f:
    line = f.read()
    line = line.strip()

print('10-1')

print(line)
print(line)
print(line)

next()
print('10-2')

line = line.replace('python', 'C#')
print(line)
line = line.replace('C#', 'Java Script')
print(line)
line = line.replace('Java Script', 'Assembly')
print(line)
