"""Advent of Code Day 5
https://adventofcode.com/2019/day/5
new Intcode computer instructions"""

with open("1205.txt") as f:
    oplist1 = f.read().split(',') #list of strings
    oplist = [int(n) for n in oplist1]
    print(oplist[:10])

def main(mylist, inp):
    """Operates on list with input inp"""
    newList = mylist[::]
    counter = 0
    while True:
        if newList[counter] in [99,99999]:
            return newList

        if newList[counter] > 100: #more than two digits
            val = quad(newList,newList[counter],newList[counter+1],newList[counter+2],
                 newList[counter+3])
            if val:
                return val
            counter += 4
        if newList[counter] == 1: #addition
            thisquad = newList[counter:counter + 4]
            print("thisquad",thisquad)
            newList[thisquad[3]] = newList[thisquad[1]] + newList[thisquad[2]]
            counter += 4
        elif newList[counter] == 2: #multiplication
            thisquad = newList[counter:counter + 4]
            newList[thisquad[3]] = newList[thisquad[1]] * newList[thisquad[2]]
            counter += 4
        elif newList[counter] == 3: #take input
            newList[newList[counter+1]] = inp
            counter += 2
        elif newList[counter] == 4: #output value at next parameter
            return newList[newList[counter + 1]]
        print("Counter: ",counter)
        print("Mylist:",newList[:20])

def quad(mylist,nums,p1,p2,p3):
    '''Operates on mylist given confusing nums'''
    numstring = str(nums)
    if len(numstring) == 4:
        m2,m1,opcode = int(numstring[-4]),int(numstring[-3]),int(numstring[-2:])
        print(m2,m1,opcode)
        if opcode == 1:
            if m1 == 0:
                addend1 = mylist[p1]
            else:
                addend1 = p1
            if m2 == 0:
                addend2 = mylist[p2]
            else:
                addend2 = p2
            mylist[p3] = addend1 + addend2

        if opcode == 2:
            if m1 == 0:
                factor1 = mylist[p1]
            else:
                factor1 = p1
            if m2 == 0:
                factor2 = mylist[p2]
            else:
                factor2 = p2
            mylist[p3] = addend1 * addend2

    else:

        m1, opcode = int(numstring[-3]), int(numstring[-2:])
        if opcode == 4:
            return mylist[0]



print(main(oplist,1))


# for a in range(1,100):
#     for b in range(1,100):
#         op = quad(oplist,a,b)
#         if op[0] == 19690720:
#             print("Solution:",a,b)
