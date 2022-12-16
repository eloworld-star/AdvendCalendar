file1 = open('file8.txt', 'r')

def addEnd(y,x):
    if end[y][x] == 0:
        end[y][x] = 1


#creation des deux matrices

nbrCol = 0
nbrLine = 0
main = []
end = []

for line in file1:
    list1 = []
    list2 = []
    temp = 0
    for element in line:
        if element != "\n":
            temp+=1
            list1.append(int(element))
            list2.append(0)
        nbrCol = temp
    nbrLine+=1
    main.append(list1)
    end.append(list2)


#passage gauche-droite
posY = 0
while posY < nbrLine:
    posX = 0
    lastSave = -1
    while posX < nbrCol:
        if main[posY][posX] > lastSave:
            lastSave = main[posY][posX]
            addEnd(posY, posX)
        posX+=1
    posY+=1

#passage droite-gauche
posY = 0
while posX < nbrLine:
    posX = nbrCol-1
    lastSave = -1
    while posX >= 0:
        if main[posY][posX] > lastSave:
            lastSave = main[posY][posX]
            addEnd(posY, posX)
        posX-=1
    posY+=1

#passage haut-bas
posX = 0
while posX < nbrCol:
    posY = 0
    lastSave = -1
    while posY < nbrLine:
        if main[posY][posX] > lastSave:
            lastSave = main[posY][posX]
            addEnd(posY, posX)
        posY+=1
    posX+=1

#passage bas-haut
posX = 0
while posX < nbrCol:
    posY = nbrLine-1
    lastSave = -1
    while posY >= 0:
        if main[posY][posX]:
            lastSave = main[posY][posX]
            addEnd(posY, posX)
        posY-=1
    posX+=1

#calcul du nombre d'arbre visible
for line in end:
    for element in line:
        if element == 1:
            total+=1

print(total)
