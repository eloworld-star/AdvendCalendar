file1 = open('file3.txt', 'r')
dict = {
'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26
,'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52
}
dictValue = dict.values()
value = 0
for line in file1:
    letterFound = ''
    taille = len(line)-1
    n=taille/2
    chunk = [line[i:i+int(n)] for i in range (0, taille, int(n))]
    #print(chunk)
    str1 = chunk[0]
    str2 = chunk[1]
    for i in str1:
        for j in str2:
            if i == j:
                letterFound=i
    for k in dict.keys():
        if letterFound == k:
            value+=dict[k]

print(value)
