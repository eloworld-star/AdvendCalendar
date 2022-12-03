file1 = open('file3.txt', 'r')
dict = {
'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26
,'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52
}
dictValue = dict.values()
stringList = []
value = 0
countLine = 0
for line in file1:
    letterFound = ''
    stringList.append(line)
    countLine+=1
    if countLine%3==0:
        print(str(countLine)+" - enter")
        str1 = stringList[0]
        str2 = stringList[1]
        str3 = stringList[2]
        for i in str1:
            for j in str2:
                for k in str3:
                    if i == j and i==k:
                        print(i+" - "+j+" - "+k)
                        print("found")
                        letterFound=i
                        break
            if letterFound!='':
                break

        for p in dict.keys():
            if letterFound == p:
                value+=dict[p]
        stringList=[]
print(value)
