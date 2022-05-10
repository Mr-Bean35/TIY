# File : 8-9, 8-10, 8-11.py
# Date : 2/16/2022
# Author : Ben Hensley Jr.

mess = ['The old rusted farm equipment surrounded the house predicting its demise.',
        'He wondered why at 18 he was old enough to go to war, but not old enough to buy cigarettes.',
        'He swore he just saw his sushi move.',
        'Waffles are always better without fire ants and fleas.',
        'Sometimes it is better to just walk away from things and go back to them later when you’re in a better frame of mind']

def showMessage():
    for items in mess:
        print(items)


showMessage()

'8-10'
print('\n')

def sendMessage():
    newList = []
    for items in mess:
        print(items)
        newList.append(items)
    print(newList)


showMessage()
sendMessage()

'8-11'
print('\n')

sendMessage()
showMessage()


