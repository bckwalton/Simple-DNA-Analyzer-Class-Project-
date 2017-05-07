def oneHamComp4(a, b):
    count = 0
    if a[0] == b[0]:
        count = count + 1
    if a[1] == b[1]:
        count = count + 1
    if a[2] == b[2]:
        count = count + 1
    if a[3] == b[3]:
        count = count + 1
    if count > 2:
        return True
    else:
        return False
listomatches = []
print('>>>>>>>>>>>>>>>>>>>>>>>')
print('>D.N.A. Analyzer Basic<')
print('<<<<<<<<<<<<<<<<<<<<<<<')
one = input('Enter the First DNA String: ')
while not one:
    one = "ACTGACGCAG"
two = input('Enter the Second DNA String: ')
while not two:
    two = "TCACAACGGG"
three = input('Enter the third DNA String: ')
while not three:
    three = "GAGTCCAGTT"
oneParts = []
twoParts = []
threeParts = []
offset = 0
while offset < 7:
        oneParts.append(one[(0+offset):(4+offset)])
        twoParts.append(two[(0+offset):(4+offset)])
        threeParts.append(three[(0+offset):(4+offset)])
        offset = offset +1
for base1 in ["A", "C", "G", "T"]:
    for base2 in ["A", "C", "G", "T"]:
        for base3 in ["A", "C", "G", "T"]:
            for base4 in ["A", "C", "G", "T"]:
                comparator = (base1 + base2 + base3 + base4)
                offset = 0
                while offset < 1:
                        count2 = 0
                        temp = 0
                        offset1 = 0
                        offset2 = 0
                        offset3 = 0
                        while (offset1 < 7):
                            if (oneHamComp4(comparator, oneParts[offset1])):
                                temp= temp + 1
                            offset1 = offset1 +1
                        if temp > 0: count2 = count2 + 1
                        temp = 0
                        while (offset2 < 7):
                            if (oneHamComp4(comparator, twoParts[offset2])):
                                temp= temp + 1
                            offset2 = offset2 + 1
                        if temp > 0: count2 = count2 + 1
                        temp = 0
                        while (offset3 < 7):
                            if (oneHamComp4(comparator, threeParts[offset3])):
                                temp= temp + 1
                            offset3 = offset3 +1
                        if temp > 0: count2 = count2 + 1
                        if (count2 == 3):
                            listomatches.append(comparator)
                        offset = offset +1
print("List of Matches within one Hamming Bit:")
print(listomatches)
