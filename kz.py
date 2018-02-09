#!/usr/bin/env python3
#Build used https://es.wikipedia.org/wiki/Signo_zodiacal
import sys
import os
from termcolor import colored


banner = """                                                                     
88      a8P                                               888888888888  
88    ,88'                                                         ,88  
88  ,88"                                                         ,88"   
88,d88'       8b,dPPYba,    ,adPPYba,   8b      db      d8     ,88"     
8888"88,      88P'   `"8a  a8"     "8a  `8b    d88b    d8'   ,88"       
88P   Y8b     88       88  8b       d8   `8b  d8'`8b  d8'  ,88"         
88     "88,   88       88  "8a,   ,a8"    `8bd8'  `8bd8'  88"           
88       Y8b  88       88   `"YbbdP"'       YP      YP    888888888888  
###################
Example:
Enter Month:
january
Enter Day:
21
###################
"""
banner = colored(banner, 'green')
print (banner)
# month
m = str(input('Enter Month\n'))
# dayy
d = int(input('Enter day\n'))

# year
#y = input ('Enter Year \n')


def main():
    if(d <= 31):
        kz()
    else:
        print('No existen mas de 31 Dias')

def kz():
            # Acuario
        if m == 'january' and d >= 21:
            zs = ('Zodiac Sign : Acuario')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign : Tiger')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        elif m == 'february' and d <= 18:
            zs = ('Zodiac Sign : Acuario')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign : Tiger')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        # Psicis
        elif m == 'february' and d >= 19:
            zs = ('Zodiac Sign : Psicis')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign : Bunny')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        elif m == 'march' and d <= 20:
            zs = ('Zodiac Sign : Psicis')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign : Bunny')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        # Aries
        elif m == 'march' and d >= 21:
            zs = ('Zodiac Sign : Aries')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign : Dragon')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        elif m == 'april' and d <= 20:
            zs = ('Zodiac Sign : Aries')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign : Dragon')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        # Tauro
        elif m == 'april' and d >= 21:
            zs = ('Zodiac Sign : Tauro')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign : Snake')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        elif m == 'may' and d <= 21:
            zs = ('Zodiac Sign : Tauro')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign : Snake')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        # Geminis
        elif m == 'may' and d >= 22:
            zs = ('Zodiac Sign : Geminis')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign : Horse')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        elif m == 'june' and d <= 20:
            zs = ('Zodiac Sign : Geminis')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign : Horse')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        # Cancer
        elif m == 'june' and d >= 21:
            zs = ('Zodiac Sign : Cancer')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign : Goat')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        elif m == 'july' and d <= 22:
            zs = ('Zodiac Sign : Cancer')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign : Goat')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        # Leo
        elif m == 'july' and d >= 23:
            zs = ('Zodiac Sign : Leo')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign : Monkey')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        elif m == 'august' and d <= 22:
            zs = ('Zodiac Sign : Virgo')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign : Rooster')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        # Virgo
        elif m == 'august' and d >= 23:
            zs = ('Zodiac Sign : Libra')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign : Dog')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        elif m == 'september' and d <= 21:
            zs = ('Zodiac Sign : Virgo')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign : Rooster')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        # Libra
        elif m == 'september' and d >= 22:
            zs = ('Zodiac Sign: Libra')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign: Dog')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        elif m == 'october' and d <= 22:
            zs = ('Zodiac Sign: Libra')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign: Dog')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        # Escorpio
        elif m == 'october' and d >= 23:
            zs = ('Zodiac Sign: Scorpion')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign: Pig')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        elif m == 'november' and d <= 22:
            zs = ('Zodiac Sign: Scorpion')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign: Pig')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)
        # Sagitario
        elif m == 'november' and d >= 23:
            zs = ('Zodiac Sign: Sagitario')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign: Rat')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        elif m == 'december' and d <= 23:
            zs = ('Zodiac Sign: Sagitario')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign: Rat')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        # Capricornio
        elif m == 'december' and d >= 22:
            zs = ('Zodiac Sign: Capricornio')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign: Cow')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        elif m == 'january' and d <= 21:
            zs = ('Zodiac Sign: Capricornio')
            zs = colored(zs, 'blue')
            cs = ('Chinese Sign: Cow')
            cs = colored(cs, 'red')
            print (zs)
            print (cs)

        else:
            print ('Sucedio un erro')


if __name__ == '__main__':
    main()
