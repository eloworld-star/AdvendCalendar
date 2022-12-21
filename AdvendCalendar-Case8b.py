file1 = open('file8.txt', 'r')


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
    while posX < nbrCol:
        nbrTreeSeen = 0
        locY = posY
        locX = posX+1
        while locX<nbrCol:
            if main[locY][locX]>=main[posY][posX]:
                nbrTreeSeen+=1
                break
            else:
                nbrTreeSeen+=1
            locX+=1
        end[posY][posX]=nbrTreeSeen
        posX+=1
    posY+=1

#passage droite-gauche

posY = 0
while posY < nbrLine:
    posX = nbrCol-1
    while posX >= 0:
        nbrTreeSeen = 0
        locY = posY
        locX = posX-1
        while locX>=0:
            if main[locY][locX]>=main[posY][posX]:
                nbrTreeSeen+=1
                break
            else:
                nbrTreeSeen+=1
            locX-=1
        end[posY][posX]*=nbrTreeSeen
        posX-=1
    posY+=1

#passage haut-bas
posX = 0
while posX < nbrCol:
    posY = 0
    while posY < nbrLine:
        nbrTreeSeen = 0
        locY = posY+1
        locX = posX
        while locY<nbrLine:
            if main[locY][locX]>=main[posY][posX]:
                nbrTreeSeen+=1
                break
            else:
                nbrTreeSeen+=1
            locY+=1
        end[posY][posX]*=nbrTreeSeen
        posY+=1
    posX+=1

#passage bas-haut
posX = 0
while posX < nbrCol:
    posY = nbrLine-1
    lastSave = -1
    while posY >= 0:
        nbrTreeSeen = 0
        locY = posY-1
        locX = posX
        while locY>=0:
            if main[locY][locX]>=main[posY][posX]:
                nbrTreeSeen+=1
                break
            else:
                nbrTreeSeen+=1
            locY-=1
        end[posY][posX]*=nbrTreeSeen
        posY-=1
    posX+=1

#cherche meillieur endroit
lastSave = 0
for line in end:
    for element in line:
        if element > lastSave:
            lastSave = element

print(lastSave)
