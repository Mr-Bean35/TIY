# File : 9-13, 9-14, 9-15, 9-16.py
# Date : 4/12/2022
# Author : Benjamin Hensley Jr.

import sys, time, math, random

def next():
    print(f'\n')


print('9-13')


class dice():

    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self):
        CNT = 0
        try:
            self.sides = int(self.sides)
        except ValueError:
            print('That is not a valid number')
            quit()
        while CNT < 10:
            roll = random.randint(1, self.sides)
            print(roll)
            CNT += 1
        print(f'\n')




di = dice(6)
di.roll_dice()
di = dice(10)
di.roll_dice()
di = dice(20)
di.roll_dice()

next()
print('9-14 & 9-15')

class lottery():

    def __init__(self):
        self.rand = ['d', 'n', 't', 'h', 'e', '43', '5', '56', '23', '14', '77', '31', '80', '22', '48']
        self.my_tickets = []
        self.winning = []

    def calling(self):
        w = (len(self.rand) - 1)
        a = self.rand[w]
        self.winning.append(a)
        x = random.choice([i for i in range(0, (len(self.rand) - 1)) if i not in [w]])
        b = self.rand[x]
        self.winning.append(b)
        y = random.choice([i for i in range(0, (len(self.rand) - 1)) if i not in [w, x]])
        c = self.rand[y]
        self.winning.append(c)
        z = random.choice([i for i in range(0, (len(self.rand) - 1)) if i not in [w, x, y]])
        d = self.rand[z]
        self.winning.append(d)

        print(f'Any four tickets with {a}, {b}, {c}, or {d} on their ticket(s) won! \n'
              f'Please come put and claim your prize!.\n')

        CNT = 0
        while CNT < 4:
            m = input('Enter 4 numbers or letters to enter the lottery: ')
            self.my_tickets.append(m)
            CNT += 1

        CNT2 = 0
        t = True
        while t == True:
            for ticket in self.my_tickets:
                for win in self.winning:
                    if ticket == win:
                        print(f'It Took {CNT2} trie(s) to pull the right numbers')
                        t = False
                        break
                else:
                    CNT2 += 1

lot = lottery()
lot.calling()






