

with open("1206.txt") as f:
    list1 = f.read().split() #list of strings
    #print
    list2 = list1[:30]

orbdict = dict()
planet_names = []
planet_set = set()

running_sum = 0


def get_num_orbits():
    for i in range(200):

        for line in list1:
            ind = line.index(')')
            planet1 = line[:ind]
            planet2 = line[(ind+1):]
            #print(planet1,planet2)
            if planet1 not in orbdict:
                orbdict[planet1] = 0
                #print("Created",planet1)
                if planet2 not in orbdict.keys():
                    orbdict[planet2] = 1
                    #print("Created",planet2)
                else:
                    #print "planet2 already"
                    orbdict[planet2] += 1
            elif planet2 not in orbdict:
                orbdict[planet2] = orbdict[planet1] + 1
                #print("Created2", planet2)
            else:
                if orbdict[planet2] != orbdict[planet1] + 1:
                    orbdict[planet2] = orbdict[planet1] + 1
                    #print("Updated", planet2)

        sum1= sum(orbdict.values())
        if sum1 > running_sum:
            running_sum = sum1
            print("Changed sum:",running_sum)
        else:
            print("Unchanged:",running_sum)
    #print(orbdict)
    print(sum(orbdict.values()))

def get_orbitals():
    """Assign every planet a list of orbitals from beginning
    then add steps from you to santa"""
    orbitals = dict()
    for line in list1:
        ind = line.index(')')
        planet1 = line[:ind]
        planet2 = line[(ind + 1):]
        if planet1 not in orbitals:
            orbitals[planet1] = [planet1]
            if planet2 not in orbitals:
                orbitals[planet2] = [planet1,planet2]
            else:
                orbitals[planet2].insert(0,planet1)
        elif planet2 not in orbitals:
            orbitals[planet2] = orbitals[planet1] + [planet2]
        else:
            orbitals[planet2] = orbitals[planet1] + orbitals[planet2]
    #print("Orbitals",orbitals)

    #fill in previous orbitals
    while True:
        first_planet = orbitals['YOU'][0]
        if len(orbitals[first_planet]) == 1:
            break
        for p in reversed(orbitals[first_planet]):
            if p not in orbitals['YOU']:
                orbitals['YOU'].insert(0,p)
                print(orbitals['YOU'])

    while True:
        first_planet = orbitals['SAN'][0]
        if len(orbitals[first_planet]) == 1:
            break
        for p in reversed(orbitals[first_planet]):
            if p not in orbitals['SAN']:
                orbitals['SAN'].insert(0, p)

    #find common planet
    rev_you = list(reversed(orbitals['YOU']))
    rev_san = list(reversed(orbitals['SAN']))
    print(rev_san,rev_you)

    for x in rev_you:
        if x in rev_san:
            print("X:",x)
            steps = rev_you.index(x) + rev_san.index(x) - 2
            break
    print(steps)

get_orbitals()