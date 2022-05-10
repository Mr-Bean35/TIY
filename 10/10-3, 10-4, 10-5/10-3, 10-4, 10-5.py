# File : 10-3, 10-4, 10-5.py
# Date : 4/18/2022
# Author : Benjamin Hensley Jr.

import sys, time, math


def next():
    print(f'\n')


print('10-3')


name = input("Enter in your name please: ")

with open('guest (10-3).txt', 'a') as f:
    f.write(f'{name.title()}\n')

next()
print('10-4')


while True:
    name = input("Enter in your name please: ")
    print(f'Hello {name.title()}. And welcome to the Jungle')
    with open('guest_book (10-4).txt', 'a') as f:
        f.write(f'{name.title()}\n')
    break

next()
print('10-5')


while True:
    why = input('Why do you like programming?: ')
    with open('response (10-5).txt', 'a')as f:
        f.write(f'{why}.\n')
    break


