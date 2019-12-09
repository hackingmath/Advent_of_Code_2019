with open("1208.txt") as f:
    oplist1 = f.read().split(',') #list of strings
    oplist = []
    for n in oplist1:
        for string in n:
            oplist.append(string)

    layers = [oplist[150 * i:150 * (i + 1)] for i in range(100)]
    layers = layers[:-1]

def part1():
    print("Length of list:",len(oplist))


    record = 150 #lowest number of zeros
    record_layer = None
    #print("Layers:",layers[:3])
    for n,layer in enumerate(layers):
        if n < 100:
            #print(n,layer)
            if layer.count('0') < record:
                record = layer.count('0')
                record_layer = n
    print("Record_layer:",n)
    print(layers[record_layer])
    ones = layers[record_layer].count('1')
    twos = layers[record_layer].count('2')
    print(ones,twos)

    print("Product:",ones * twos)

    #print(oplist[:10])

def check_pixel(a,i):
    """Goes through layers in list a
    and returns value for pixel i"""

    for layer in a:
        if layer[i] == '2':
            continue
        if layer[i] == '1':
            return 'X'
        if layer[i] == '0':
            return " "
    #If it's only 2's ?
    return '.'


def part2():
    output = ''
    for i in range(150):
        output += check_pixel(layers,i)
    print("Length of output",len(output))

    for k in range(6):
    #     outstr = ''
    #for j in range():
        print(output[25*k:25*(k+1)])


part2()
"""FSJUZ"""