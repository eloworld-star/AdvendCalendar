resultFinal = 0
lastValueTemp = 75502
totalCalories = 0
packMostCalories = 0

i=0
while i<3:
    file1 = open('file.txt', 'r')
    for line in file1:
        if line == "\n":
            if totalCalories>packMostCalories and totalCalories<lastValueTemp:
                packMostCalories=totalCalories
            totalCalories=0
        else:
            totalCalories+=int(line)
    file1.close()

    lastValueTemp=packMostCalories
    resultFinal+=lastValueTemp
    packMostCalories=0
    totalCalories=0
    i+=1
print(resultFinal)
