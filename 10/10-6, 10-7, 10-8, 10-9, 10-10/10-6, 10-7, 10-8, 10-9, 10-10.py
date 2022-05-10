# File : 10-6, 10-7, 10-8, 10-9, 10-10.py
# Date : 4/19/2022
# Author : Benjamin Hensley Jr.

import sys, time, math


def next():
    print(f'\n')


print('10-6 & 10-7')


"""while True:
    A = input('Enter A Number: ')
    try:
        A = int(A)
        break
    except ValueError:
        print('Please enter a number')

while True:
    B = input('Enter A Second Number: ')
    try:
        B = int(B)
        break
    except ValueError:
        print('Please enter a number')

print(A*B)
"""
next()
print('10-8 & 10-9')


try:
    with open('cats.txt') as f:
        cat = f.read()
        cat = cat.strip()
        print(cat)
except FileNotFoundError:
    pass # print('That file does not exist')

try:
    with open('dogs.txt') as e:
        dog = e.read()
        dog = dog.strip()
        print(dog)
except FileNotFoundError:
    pass # print(f'That file does not exist')

next()
print('10-10')


with open('Article_1.txt', 'r', encoding='utf-8') as f:
    art1 = f.read()
    print(art1.count('the'))


with open('Article_2.txt', 'r', encoding='utf-8') as e:
    art2 = e.read()
    print(art2.count('as'))







