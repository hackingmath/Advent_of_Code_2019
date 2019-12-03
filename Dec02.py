"""Advent of Code Day 2"""

with open("1202.txt") as f:
    oplist1 = f.read().split(',') #list of strings
    oplist = [int(n) for n in oplist1]

def quad(mylist,a,b):
    """Operates on 4-value list"""
    newList = mylist[::]
    newList[1] = a
    newList[2] = b
    counter = 0
    while True:
        if newList[4*counter] == 99:
            return newList
        thisquad = newList[4*counter:4*counter+4]
        if thisquad[0] == 1:
            newList[thisquad[3]] = newList[thisquad[1]] + newList[thisquad[2]]
        elif thisquad[0] == 2:
            newList[thisquad[3]] = newList[thisquad[1]] * newList[thisquad[2]]
        counter += 1


for a in range(1,100):
    for b in range(1,100):
        op = quad(oplist,a,b)
        if op[0] == 19690720:
            print("Solution:",a,b)
