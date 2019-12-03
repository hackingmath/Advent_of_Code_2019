'''Advent of Code Day 1
December 1, 2019
Fuel for Modules'''

def fuel(mass):
    """Simple mass calculation"""
    return mass//3 - 2

def fuel2(mass):
    """Mass is put into fuel() until 0"""
    output = 0
    f = fuel(mass)
    while f > 0:
        output += f
        f = fuel(f)
    return output

with open("1201.txt") as f:
    modlist = f.read().split() #list of strings
    print(sum([fuel2(int(n)) for n in modlist]))


