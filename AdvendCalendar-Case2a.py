def NbrPtsShape(val):
    if val == 'X':
        return 1
    elif val == 'Y':
        return 2
    else:
        return 3

val1=''
val2=''
total = 0

file1 = open('file2.txt', 'r')
for line in file1:
    val1 = line.split()[0]
    val2 = line.split()[1]
    #case win
    if val1 == 'A' and val2 == 'Y' or val1 == 'C' and val2 == 'X' or val1 == 'B' and val2 == 'Z':
        total += 6 + NbrPtsShape(val2)
    #case lose
    elif val1 == 'B' and val2 == 'X' or val1 == 'A' and val2 == 'Z' or val1 == 'C' and val2 == 'Y':
        total += 0 + NbrPtsShape(val2)
    #case draw
    elif val1 == 'B' and val2 == 'Y' or val1 == 'A' and val2 == 'X' or val1 == 'C' and val2 == 'Z':
        total += 3 + NbrPtsShape(val2)
print(total)
