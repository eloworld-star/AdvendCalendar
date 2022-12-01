
resultFinal = 0
lastValueTemp1 = 0
lastValueTemp2 = 0
totalCalories = 0
packMostCalories = 0

print("start")
count = 0
i=0
while i<3:


    file1 = open('file.txt', 'r')
    for line in file1:
        if line == "\n":
            #print("====================================")
            count+=1
            #print("retour")
            #print("------------------------")
            #print(totalCalories)

            if totalCalories>packMostCalories and totalCalories!=lastValueTemp1 and totalCalories!=lastValueTemp2:
                packMostCalories=totalCalories
            #    print("------------------------")
            #    print(packMostCalories)
            #    print("------------------------")
            totalCalories=0
            #print("====================================")
        else:
            totalCalories+=int(line)
        #print(line.strip())
    file1.close()

    #input("continue ? ")


    if i==0:
        lastValueTemp1=packMostCalories
        print("+++++++++++++++++++++++++++++++++++++")
        print(lastValueTemp1)
    elif i==1:
        lastValueTemp2=packMostCalories
        print("+++++++++++++++++++++++++++++++++++++")
        print(lastValueTemp2)
    else:
        print("+++++++++++++++++++++++++++++++++++++")
        print(packMostCalories)
    print("+++++++++++++++++++++++++++++++++++++")
    totalCalories
    packMostCalories=0

    i+=1


#print("++++++++++++++++++++++++++++++++++++++++++")
#lastValueTemp = packMostCalories
#print(packMostCalories)
