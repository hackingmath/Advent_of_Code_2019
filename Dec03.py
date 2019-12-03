"""Advent of Code Day 3"""

import time

start = time.time()

def locations(mylist):
    """returns list of locations from
    directions in mylist"""
    loc = [0,0]
    locs = list()
    for d in mylist:
        if d[0] == 'R':
            distance = int(d[1:])
            for i in range(1,distance+1):
                loc = [loc[0]+1,loc[1]]
                if loc not in locs:
                    locs.append(loc)
        if d[0] == 'L':
            distance = int(d[1:])
            for i in range(1,distance+1):
                loc = [loc[0] - 1, loc[1]]
                if loc not in locs:

                    locs.append(loc)
        if d[0] == 'D':
            distance = int(d[1:])
            for i in range(1,distance+1):
                loc = [loc[0], loc[1]-1]
                if loc not in locs:

                    locs.append(loc)
        if d[0] == 'U':
            distance = int(d[1:])
            for i in range(1,distance+1):
                loc = [loc[0], loc[1]+1]
                if loc not in locs:

                    locs.append(loc)
    return locs

def locations2(mylist,list2):
    """calculates locations from
    directions in mylist, adds to intersections
    list if in list2"""
    loc = [0,0]
    inters = list()
    for d in mylist:
        if d[0] == 'R':
            distance = int(d[1:])
            for i in range(1,distance+1):
                loc = [loc[0]+1,loc[1]]
                if loc in list2:
                    inters.append(loc)
        if d[0] == 'L':
            distance = int(d[1:])
            for i in range(1,distance+1):
                loc = [loc[0] - 1, loc[1]]
                if loc in list2:
                    inters.append(loc)
        if d[0] == 'D':
            distance = int(d[1:])
            for i in range(1,distance+1):
                loc = [loc[0], loc[1]-1]
                if loc in list2:
                    inters.append(loc)
        if d[0] == 'U':
            distance = int(d[1:])
            for i in range(1,distance+1):
                loc = [loc[0], loc[1]+1]
                if loc in list2:
                    inters.append(loc)
    return inters

def locations_steps(mylist):
    """returns list of locations from
    directions in mylist"""
    steps = 0
    loc = [0,0,0]
    locs = dict()
    for d in mylist:
        if d[0] == 'R':
            distance = int(d[1:])
            for i in range(1,distance+1):
                steps += 1
                loc[0] += 1
                locs[(loc[0],loc[1])] = steps

        if d[0] == 'L':
            distance = int(d[1:])
            for i in range(1,distance+1):
                steps += 1
                loc[0] -= 1
                locs[(loc[0], loc[1])] = steps

        if d[0] == 'D':
            distance = int(d[1:])
            for i in range(1,distance+1):
                steps += 1
                loc[1] -= 1
                locs[(loc[0], loc[1])] = steps

        if d[0] == 'U':
            distance = int(d[1:])
            for i in range(1,distance+1):
                steps += 1
                loc[1] += 1
                locs[(loc[0], loc[1])] = steps

    return locs

def locations2_steps(mylist,a):
    """calculates locations from
        directions in mylist, adds to intersections
        list if in list2"""
    steps = 0
    loc = [0, 0, 0]
    inters = dict()
    for d in mylist:
        if d[0] == 'R':
            distance = int(d[1:])
            for i in range(1, distance + 1):
                steps += 1
                loc[0] += 1
                thisloc = (loc[0], loc[1])
                if thisloc in a.keys():
                    inters[thisloc] = steps + a[thisloc]

        if d[0] == 'L':
            distance = int(d[1:])
            for i in range(1, distance + 1):
                steps += 1
                loc[0] -= 1
                thisloc = (loc[0], loc[1])
                if thisloc in a.keys():
                    inters[thisloc] = steps + a[thisloc]

        if d[0] == 'D':
            distance = int(d[1:])
            for i in range(1, distance + 1):
                steps += 1
                loc[1] -= 1
                thisloc = (loc[0], loc[1])
                if thisloc in a.keys():
                    inters[thisloc] = steps + a[thisloc]

        if d[0] == 'U':
            distance = int(d[1:])
            for i in range(1, distance + 1):
                steps += 1
                loc[1] += 1
                thisloc = (loc[0], loc[1])
                if thisloc in a.keys():
                    inters[thisloc] = steps + a[thisloc]

    return inters

def intersections(a,b):
    """Returns list of all points common to lists a and b"""
    return [d for d in locations(a) if d in locations(b)]

def closest(lista):
    output = abs(lista[0][0]) + abs(lista[0][1])
    for loc in lista:
        distance = abs(loc[0]) + abs(loc[1])
        if distance < output:
            output = distance
    return output


with open("1203.txt") as f:
    wirelist1 = f.read().split() #list of strings
    wirelist = [n.split(',') for n in wirelist1]

l1 = ['R8','U5','L5','D3']

l2 = ['U7','R6','D4','L4']

a = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
b = ['U62','R66','U55','R34','D71','R55','D58','R83']

c = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
d = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

p = wirelist[0]
#print("P:",p[:10])
q = wirelist[1]
#print("Q:",q[:10])

#print(intersections(a,b))

#get all locations in trail of a
step1 = locations_steps(p)
print("Completed step 1")
#get list of intersections with b
step2 = locations2_steps(q,step1)
print("Completed step 2")
#print(step2)
print("Min:",min(step2.values()))

print("Time (secs):", round(time.time()-start,1))
