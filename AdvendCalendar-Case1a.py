totalCalories = 0
packMostCalories = 0


file1 = open('file.txt', 'r')
count = 0

for line in file1:
    if line == "\n":
        if totalCalories>packMostCalories:
            packMostCalories=totalCalories
        totalCalories=0
    else:
        totalCalories+=int(line)
print(packMostCalories)
file1.close()
