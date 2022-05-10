# File : Employee.py
# Date : 4/20/2022
# Author : Benjamin Hensley Jr.

import sys, time, math

class Employee():

    def __init__(self, first, last, salary, raisef = 5000):
        self.first = first.title()
        self.last = last.title()
        self.salary = salary
        self.raisef = raisef
        try:
            self.salary = int(self.salary)
        except ValueError:
            print("That is an invalid salary")
        self.hourly = self.salary/12/4/40
        self.hourly = round(self.hourly, 2)

    def greetUser(self):
        print(f'You are {self.last}, {self.first} and you make {self.salary} annually.\n'
              f'Which is approximately {self.hourly} per hour\n')


    def giveRaise(self):
        try:
            self.raisef = int(self.raisef)
        except ValueError:
            print("That is an invalid amount to raise the salary")
        self.salary += self.raisef
        self.hourly = self.salary/12/4/40
        self.hourly = round(self.hourly, 2)
        print(f'Hello {self.last}, {self.first}. Congrats you got a {self.raisef} dollar yearly raise\n'
              f'You now make {self.salary} which is approximately {self.hourly} per hour')



Me = Employee('Ben', 'Hensley', '28358')
Me.greetUser()
Me.giveRaise()




