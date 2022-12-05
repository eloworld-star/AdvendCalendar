dict = {1:['H','R','B','D','Z','F','L','S'],
        2:['T','B','M','Z','R'],
        3:['Z','L','C','H','N','S'],
        4:['S','C','F','J'],
        5:['P','G','H','W','R','Z','B'],
        6:['V','J','Z','G','D','N','M','T'],
        7:['G','L','N','W','F','S','P','Q'],
        8:['M','Z','R'],
        9:['M','C','L','G','V','R','T']}


file1 = open('file5.txt', 'r')
for line in file1:
    chunk=line.split()
    nbrMove = int(chunk[1])
    fromCol = int(chunk[3])
    toCol = int(chunk[5])
    tabFrom = dict[fromCol]
    tabTo = dict[toCol]

    print(nbrMove)
    print("-")
    print(fromCol)
    print(tabFrom)
    print("-")
    print(toCol)
    print(tabTo)
    print("-")


    lenght=len(tabFrom)
    partToMove = tabFrom[lenght-nbrMove:lenght]
    i=0
    while i<nbrMove:
        tabFrom.pop(lenght-nbrMove)
        i+=1
        
    #enlever le # a la ligne suivante pour la partie A
    #partToMove.reverse()
    for element in partToMove:
        tabTo.append(element)

    print("partToMove")
    print(partToMove)
    print("new tab "+str(toCol))
    print(tabTo)
    print("new tab"+str(fromCol))
    print(tabFrom)
    print("======================================")
print(dict)
