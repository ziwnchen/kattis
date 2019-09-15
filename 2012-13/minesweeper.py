import sys

def count_mine(i, j):
    if field[i][j]==1:
        return -1
    else:
        try:
            n2 = field[i - 1][j - 1]
            if (i-1<0) | (j-1<0):
                n2=0
        except IndexError:
            n2 = 0
        try:
            n3 = field[i - 1][j]
            if i-1<0:
                n3=0
        except IndexError:
            n3 = 0
        try:
            n4 = field[i - 1][j + 1]
            if i-1<0:
                n4=0
        except IndexError:
            n4 = 0
        try:
            n5 = field[i][j - 1]
            if (j-1<0):
                n5=0
        except IndexError:
            n5 = 0
        try:
            n6 = field[i][j + 1]
        except IndexError:
            n6 = 0
        try:
            n7 = field[i + 1][j - 1]
            if (j-1<0):
                n7=0
        except IndexError:
            n7 = 0
        try:
            n8 = field[i + 1][j]
        except IndexError:
            n8 = 0
        try:
            n9 = field[i + 1][j + 1]
        except IndexError:
            n9 = 0
        total = n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
        return total

data=sys.stdin.readlines()
para=data[0].split()
x=int(para[0])
y=int(para[1])

field=[]
for line in data[1:]:
    row=list(map(int, line.split()))
    field.append(row)

for i in range(x):
    #print("\n")
    new_row=[]
    for j in range(y):
        mine_number=count_mine(i,j)
        if mine_number== 0:
            new_value='-'
        elif mine_number==-1:
            new_value="X"
        else:
            new_value=mine_number
        new_row.append(new_value)
    print(*new_row, sep="")
