# File : 8-12, 8-13, 8-14.py
# Date : 3/15/2022
# Author : Ben Hensley Jr.
def next():
    print('\n')


"8-12"
def sandwich():
    test = True
    test2 = True
    items = []
    while test == True:
        if test2 == True:
            inp = input('What Would You Like On Your Sandwich? (Type q to stop): ')
            if inp == 'q' or inp == 'Q':
                break
            else:
                items.append(inp)
                test2 = False
        else:
            inp = input('Anything else? (Type q to stop): ')
            if inp == 'q' or inp == 'Q':
                break
            else:
                items.append(inp)
    print('So You Would Like A Sandwich With:')
    for i in items:
        i.title()
        print(i)

# sandwich()
next()

"8-13"
def build_profile(first, last, **user_info):

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Ben', 'Hensley Jr.',
                            location='Lakewood',
                            field='Cyber Security')

print(user_profile)
next()

"8-14"


def cars(Year=2003, Make='Toyota', Model='Highlander', Color='White'):
    car = {'Year': Year,
           'Make': Make,
           'Model': Model,
           'Color': Color}
    print(car)

cars()
cars(2007, 'Mazda', 'CX-9', 'Blue')






