# File : 8-3, 8-4, 8-5.py
# Date : 2/14/2022
# Author : Ben Hensley Jr.

def makeShirt(Text = 'I Love Python', Size = 'Large'):
    print(f'I love my shirt that says {Text} and is in {Size} size.')

makeShirt()
makeShirt('Hello World', 'XXL')


"8-3"
print('\n')


makeShirt()
makeShirt(Size = 'Medium')
makeShirt('E', 'XXXXXXXXXXXXXXXXS')


"8-5"
print('\n')

def desCity(City = 'Ottawa', Country = 'Canada'):
    print(f'{City} is in {Country}')


desCity()
desCity('Columbus', 'United States')
desCity('Split', 'Croatia')
desCity('Palermo', 'Italy')
