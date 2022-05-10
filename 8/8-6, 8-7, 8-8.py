# File : 8-6, 8-7, 8-8.py
# Date : 2/14/2022
# Author : Ben Hensley Jr.

def cityCountry(City = 'London', Country = 'England'):
    print(f'{City}, {Country}')

cityCountry()
cityCountry('Kigali', 'Rwanda')
cityCountry('Monaco', 'Monaco')
cityCountry('Ulaanbaatar', 'Mongolia')


"8-7"
print('\n')


def makeAlbum(Artist_Name, Artist_Album, NumOfSongs = 0):
    Album = {'Artist Name': Artist_Name,
             'Artist Album': Artist_Album,
             'Number Of Songs': NumOfSongs}
    if NumOfSongs != 0:
        print(f'{Artist_Name} created {Artist_Album}. And Has {NumOfSongs} Songs in the track')
    else:
        print(Artist_Name + ' created ' + Artist_Album)


makeAlbum('The Beatles', 'Abbey Road', 17)
makeAlbum('Journey', 'Departure')
makeAlbum('Benny Goodman', 'Ken Burns Jazz: Benny Goodman')

'8-8'
print('\n')

e = 'false'
while e == 'false':
    X = input('Artist Name: ')
    Y = input('Artist Album: ')
    Z = input('Track Number Here If You Know It(If You Dont Know Type q): ')
    if Z == 'q' or Z == 'Q':
        makeAlbum(X, Y)
        e = 'true'
    try:
        Z = int(Z)
    except:
        print('That is not a valid number')
        Z = input('Track Number Here If You Know It(If You Dont Know Type q):')
    makeAlbum(X, Y, Z)
    e = 'true'

