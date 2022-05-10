# File : cityFunctions.py
# Date : 4/20/2022
# Author : Benjamin Hensley Jr.

import sys, time, math

"""class cityCountry():

    def __init__(self, city, country):
        self.city = city
        self.country = country

    def readCity(self):
        print(f'{self.city}, {self.country}')"""


print(f'11-2')


def testCityCountry():
    print('Test Successful')

def testCityCountryPop():
    print('Second Test Successful')

class cityCountry():

    def __init__(self, city, country, population = ''):
        self.city = city
        self.country = country
        self.pop = population

    def readCity(self):
        if self.pop != '':
            print(f'{self.city}, {self.country} - population {self.pop}')
            testCityCountryPop()
        else:
            print(f'{self.city}, {self.country}')
            testCityCountry()


