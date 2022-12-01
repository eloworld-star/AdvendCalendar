
nbrElves = 0
noElvesMostCalories = 0
totalCalories = 0
packMostCalories = 0


file1 = open('file.txt', 'r')
count = 0

for line in file1:
    if line == "\n":
        print("retour")
        print("------------------------")
        print(totalCalories)
        print("------------------------")
        if totalCalories>packMostCalories:
            packMostCalories=totalCalories
        print(packMostCalories)
        print("------------------------")
        totalCalories=0
    else:
        totalCalories+=int(line)
    print(line.strip())

print("++++++++++++++++++++++++++++++++++++++++++")
print(packMostCalories)
file1.close()
