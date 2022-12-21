import numpy as np
file1 = open('file9.txt', 'r')
maxMov = 0
right = 0
left = 0
up = 0
down = 0
for lines in file1:
    block = lines.split()
    if int(block[1]) > maxMov:
        maxMov=int(block[1])
    elif block[0] == 'R':
        right+=int(block[1])
    elif block[0] == 'L':
        left+=int(block[1])
    elif block[0] == 'U':
        up+=int(block[1])
    else:
        down+=int(block[1])


#look for max value
max = max(right, left, up, down)
taille = 0
millieu = 0
if max%2==0:
    taille=(max*2)+1
    millieu=max+1
else:
    taille=max*2
    millieu=max

print("maxmov : "+str(maxMov))
print("right : "+str(right))
print("left : "+str(left))
print("up : "+str(up))
print("down : "+str(down))
print("max : "+str(max))
print("=====================")
print("taille : "+str(taille))
print("millieu : "+str(millieu))

print("+++++++++++++++++++++++++++++++")

#creation matrice
matrice = np.zeros([taille, taille], dtype='<U1')
matrice.fill('-')
matrice[millieu, millieu]='S'

#ajout des deplacements
# + au line quand right
# - au line quand left
# + au col quand up
# - au col quand down


file1 = open('file9.txt', 'r')
lastHeadPosX = millieu
lastHeadPosY = millieu
lastTailPosX = millieu
lastTailPosY = millieu

#remplissage du passage
for l in file1:
    chunk = l.split()
    if chunk[0]=='R':
        for i in range(int(chunk[1])):
            lastHeadPosX+=1
            #lastTailPosX+=1
            if (lastHeadPosX-lastTailPosX)==2:
                lastTailPosY=lastHeadPosY
                lastTailPosX=lastHeadPosX-1
                matrice[lastTailPosY][lastTailPosX]='#'
            #matrice[lastHeadPosY][lastHeadPosX]='$'
            #matrice[lastTailPosY][lastTailPosX]='#'
    elif chunk[0]=='L':
        for i in range(int(chunk[1])):
            lastHeadPosX-=1
            #lastTailPosX-=1
            if (lastTailPosX-lastHeadPosX)==2:
                lastTailPosY=lastHeadPosY
                lastTailPosX=lastHeadPosX+1
                matrice[lastTailPosY][lastTailPosX]='#'

            #matrice[lastHeadPosY][lastHeadPosX]='$'

    elif chunk[0]=='U':
        for i in range(int(chunk[1])):
            lastHeadPosY-=1
            #matrice[lastHeadPosY][lastHeadPosX]='$'
            if (lastTailPosY-lastHeadPosY)==2:
                lastTailPosX=lastHeadPosX
                lastTailPosY=lastHeadPosY+1
                matrice[lastTailPosY][lastTailPosX]='#'
    else:
        for i in range(int(chunk[1])):
            lastHeadPosY+=1
            #matrice[lastHeadPosY][lastHeadPosX]='$'
            if (lastHeadPosY-lastTailPosY)==2:
                lastTailPosX=lastHeadPosX
                lastTailPosY=lastHeadPosY-1
                matrice[lastTailPosY][lastTailPosX]='#'

#print(matrice)
print("+++++++++++++++++++++++++++++++")
print(np.count_nonzero(matrice=='#'))
print(np.count_nonzero(matrice=='S'))
