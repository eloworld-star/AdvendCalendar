file1 = open('file6.txt', 'r')
for line in file1:
    i=0
    found = False
    nbrOfPack=14
    print(len(line))
    while not found:
        partToCheck = line[i:i+nbrOfPack]
        print(partToCheck+" "+str(i)+"-"+str(i+nbrOfPack))
        seen = []
        for element in partToCheck:
            if element in seen:
                break
            else:
                seen.append(element)

        if len(seen)==len(partToCheck):
            found=True

        i+=1

        #if partToCheck[0]==partToCheck[1] or partToCheck[0]==partToCheck[2] or partToCheck[0]==partToCheck[3]:
        #    found=False
        #elif partToCheck[1]==partToCheck[2] or partToCheck[1]==partToCheck[3]:
        #    found=False
        #elif partToCheck[2]==partToCheck[3]:
        #    found=False
        #else:
        #    found=True
        #    print("found")
