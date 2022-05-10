# File : 9-1, 9-2, 9-3.py
# Date : 3/15/2022
# Author : Ben Hensley Jr.

print('9-1')
def next():
    print('\n')

class Restaurant():

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_rest(self):
        print(f'Here at {self.name} we have {self.type} options')

    def open(self):
        print(f'{self.name} is now open for business')

Rest = Restaurant('Wendys', 'Fast Food')
Rest.describe_rest()
Rest.open()

next()
print('9-2')

Rest = Restaurant('TStreet', 'Dine In')
Rest.describe_rest()
Rest = Restaurant('Hanger101', 'Bar & Grill')
Rest.describe_rest()
Rest = Restaurant("Dave n' Busters", "Arcade & Food")
Rest.describe_rest()

next()
print('9-3')

class User():

    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def describe(self):
        print(f"{self.last_name}, \n"
              f"{self.first_name}, \n"
              f"{self.age} years old \n"
              f"Currently resides in {self.country}")

    def greet(self):
        print(f"Hello {self.last_name}, {self.first_name}. How are you today. How is {self.country}? Is the weather good?")


Use = User('Ben', 'Hensley', '16', 'USA')
Use.describe()
Use.greet()
next()

Use = User('Tim', 'Rice', '18', 'USA')
Use.describe()
Use.greet()
next()

Use = User('Josh', 'Gomez', '19', 'England')
Use.describe()
Use.greet()



