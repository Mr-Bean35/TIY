# File : 9-10, 9-11, 9-12.py
# Date : 4/12/2022
# Author : Benjamin Hensley Jr.

import sys, time, math
from Restaurant import *
from Admin import *
from Users import *


def next():
    print(f'\n')


print('9-10')

Rest = Restaurant('hello', 'world')
Rest.serve()

next()
print('9-11')

Ad = Admin('Benjamin', 'Hensley Jr', '16', 'USA')
Ad.show_privileges()

next()
print('9-12')

Ad.show_privileges()
