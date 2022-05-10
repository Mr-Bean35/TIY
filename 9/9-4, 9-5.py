# File : 9-4, 9-5.py
# Date : 4/5/2022
# Author : Ben Hensley Jr.

import sys, time, math

print('9-4')
def next():
    print('\n')

class Restaurant():

    def __init__(self, name, type, served):
        self.name = name
        self.type = type
        self.served = served
        self.served = 0

    def describe_rest(self):
        print(f'Here at {self.name} we have {self.type} options')

    def open(self):
        print(f'{self.name} is now open for business')

    def serve(self):

        print(f"{self.name} has served {self.served} person(s)")

rest = Restaurant('Warren Tech Central', 'Sit And Wait', 0)
rest.serve()
rest.served = 1
rest.serve()

next()
print('9-5')

class User():

    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login = 0

    def describe(self):
        print(f"{self.last_name}, \n"
              f"{self.first_name}, \n"
              f"{self.age} years old \n"
              f"Currently resides in {self.country}")

    def greet(self):
        print(f"Hello {self.last_name}, {self.first_name}. How are you today. How is {self.country}? Is the weather good?")

    def incre_login_attempts(self):
        self.login += 1

    def re_login_attempts(self):
        self.login = 0

    def read_attempt(self):
        print(self.login)

use = User('Benjamin', 'Hensley', '16', 'USA')
use.incre_login_attempts()
use.incre_login_attempts()
use.incre_login_attempts()
use.incre_login_attempts()
use.read_attempt()
use.re_login_attempts()
use.read_attempt()
