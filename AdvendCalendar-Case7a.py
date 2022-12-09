file1 = open('file7.txt', 'r')
print(type(file1))
blank = "-"
packBlank = " "
plus = "+"
packPus=" "
lastSaveChunk = ""
count = 0
j=0
totalFolder=0
lvlDepth = 0

file1 = open('file7.txt', 'r')
for line in file1:
    chunk = line.split()
    if chunk[0]=="$" and chunk[1]=="cd":
        if chunk[2]!="..":
            print(str(lvlDepth)+" dir : "+chunk[2])
            lvlDepth+=1
        if chunk[2]=="..":
            lvlDepth-=1
