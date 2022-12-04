file1 = open('file4.txt', 'r')
count=0
for line in file1:
    chunk=line.split(',')
    firstPart=chunk[0].split('-')
    secondPart=chunk[1].split('-')
    print(str(firstPart[0])+" ++ "+str(firstPart[1])+" ===== "+str(secondPart[0])+" ++ "+str(secondPart[1]))
    numberOneDown = int(firstPart[0])
    numberOneUp = int(firstPart[1])
    numberTwoDown = int(secondPart[0])
    numberTwoUp = int(secondPart[1])


    if numberTwoDown>=numberOneDown and numberTwoUp<=numberOneUp:
        print("secondPart incluse dans firstPart")
        count+=1
    elif numberOneDown>=numberTwoDown and numberOneUp<=numberTwoUp:
        print("firstPart incluse dans secondPart")
        count+=1
    print("=================================================")
print(count)
