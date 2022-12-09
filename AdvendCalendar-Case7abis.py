lvlDepth = 0
maxDepth = 0

total = 0

#get the max depth
file1 = open('file7.txt', 'r')
for line in file1:
    chunk = line.split()
    if chunk[0]=="$" and chunk[1]=="cd":
        if chunk[2]!="..":
            lvlDepth+=1
        if chunk[2]=="..":
            lvlDepth-=1

    if lvlDepth>maxDepth:
        maxDepth=lvlDepth

totalFolder=0
lvlDepth = 0
unUsedSpace =0
spaceNeedToDelete=0
spaceToDelete = 0
lastSave=70000000
i=0

try:
    while i<maxDepth: #for every lvl of depth
        file1 = open('file7.txt', 'r')
        #loop on all the file
        for line in file1:
            chunk = line.split()
            if chunk[0]=="$" and chunk[1]=="cd":
                if chunk[2]!="..":
                    if i==1 and lvlDepth==0:
                        unUsedSpace = 70000000-totalFolder
                        print("unUsedSpace : "+str(unUsedSpace))
                        spaceNeedToDelete = 30000000-unUsedSpace
                        print("spaceNeedToDelete : "+str(spaceNeedToDelete))
                    if lvlDepth==i:
                        if totalFolder<100000:
                            total+=totalFolder
                        if totalFolder>=spaceNeedToDelete:
                            print("-----------------------------------------------------------------------------------------")
                            lastSave=totalFolder
                        print("           total : "+str(totalFolder))
                        print(str(lvlDepth)+" lvlDepth - dir : "+chunk[2])
                        totalFolder=0
                    lvlDepth+=1
                elif chunk[2]=="..":
                    lvlDepth-=1
            elif chunk[0].isnumeric() and lvlDepth>i:
                totalFolder+=int(chunk[0])
        #totalFolder fin du fichier
        print("           -total : "+str(totalFolder))
        if totalFolder<100000:
            total+=totalFolder
        if totalFolder>=spaceNeedToDelete:
            print("-----------------------------------------------------------------------------------------")
            lastSave=totalFolder
        i+=1
        lvlDepth = 0
        print("++++++++++++++++++++++++++++++++++++++++++++++")
    print("=====================================")
    print(total)
    print(lastSave)
    print("=====================================")


except Exception as e:
    print(e)
finally:
    print("script finish")
