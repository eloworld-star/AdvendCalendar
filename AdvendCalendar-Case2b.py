def NbrPtsShape(val):
    if val == "Rock":
        return 1
    elif val == "Paper":
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

    if val2 == 'X':
        total += 0
        if val1 == 'B':
            total += NbrPtsShape("Rock")
        elif val1 == 'A':
            total += NbrPtsShape("Scissor")
        else:
            total += NbrPtsShape("Paper")
    elif val2 == 'Y':
        total += 3
        if val1 == 'B':
            total += NbrPtsShape("Paper")
        elif val1 == 'A':
            total += NbrPtsShape("Rock")
        else:
            total += NbrPtsShape("Scissor")
    elif val2 == 'Z':
        total += 6
        if val1 == 'B':
            total += NbrPtsShape("Scissor")
        elif val1 == 'A':
            total += NbrPtsShape("Paper")
        else:
            total += NbrPtsShape("Rock")
print(total)
