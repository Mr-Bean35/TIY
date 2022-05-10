# File : 9-6, 9-7, 9-8, 9-9.py
# Date : 4/5/2022
# Author : Ben Hensley Jr.

import sys, time, math


def next():
    print(f'\n')


print('9-6')

class IceCreamStand():


    def __init__(self, name, type,):
        self.name = name
        self.type = type
        self.served = 0

    def describe_rest(self):
        print(f'Here at {self.name} we have {self.type} options')

    def open(self):
        print(f'{self.name} is now open for business')

    def serve(self):
        print(f"{self.name} has served {self.served} person(s)")

    def flavors(self):
        self.flavors = ['Chocolate', 'Vanilla', 'Mint', "Cookies N' Cream", 'Cookie Dough']
        print(f'We have:')
        CNT = 0
        for i in self.flavors:
           if CNT + 1 >= len(self.flavors):
            print(f'And {i}')
           else:
            print(i)
            CNT += 1

ice = IceCreamStand('Ben & Jerry', 'Ice Cream')
ice.flavors()

next()
print('9-7')

class Admin():

    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login = 0
        self.privileges = ['edit', 'write', 'delete']

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

    def show_privileges(self):
        e = True
        CNT = 0
        for i in self.privileges:
            if e == True:
                print(f'{self.last_name}, {self.first_name} has the privilege to:')
                print(i)
                CNT += 1
                e = False
            else:
                print(i)
                CNT += 1


admin = Admin('Benjamin', 'Hensley', '16', 'USA')
admin.show_privileges()

next()
print('9-8')

class privileges():

    def __init__(self):
        self.privileges = privileges
        self.privileges = ['edit', 'write', 'delete']


    def show_privileges(self):
        print('An Admin can:')
        for i in self.privileges:
            print(i)

priv = privileges()
priv.show_privileges()

next()
print('9-9')










