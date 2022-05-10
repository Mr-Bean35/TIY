# File : 10-11, 10-12, 10-13.py
# Date : 4/19/2022
# Author : Benjamin Hensley Jr.

import sys, time, math, json

def next():
    print(f'\n')

print('10-11')

num = input('Enter Your Favorite Number: ')

with open('favorite_number.txt', 'w') as f:
    json.dump(num, f)

next()
print('10-12')


num = input('Enter Your Favorite Number: ')

with open('favorite_number.txt', 'w') as f:
    json.dump(num, f)
    print(f'Your favorite number is {num}')

next()
print('10-13')


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    username = get_stored_username()
    Ask = input(f'Is {username} your name? Y/N?: ')
    if Ask == 'Y':
        if username:
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        get_new_username()
        greet_user()

greet_user()
