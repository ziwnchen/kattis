import sys

def make_decision(x,y,h):
    if x==0 & x!=(size[0]-1):
        h2=map[x][y+1]
        h3=map[x+1][y+1]
        c_h2=abs(h2-h)
        c_h3=abs(h3-h)
        if c_h2<=c_h3:
            return x,y+1,c_h2
        else:
            return x+1,y+1,c_h3
    elif x==(size[0]-1) & x!=0:
        h1=map[x-1][y+1]
        h2=map[x][y+1]
        c_h2=abs(h2-h)
        c_h1=abs(h1-h)
        if h2<=h1:
            return x,y+1,c_h2
        else:
            return x-1,y+1,c_h1
    elif x==(size[0]-1) & x==0:
        h2=map[x][y+1]
        c_h2 = abs(h2 - h)
        return x,y+1,c_h2
    else:
        h1=map[x-1][y+1]
        h2=map[x][y+1]
        h3=map[x+1][y+1]
        c_h1=abs(h1-h)
        c_h2=abs(h2-h)
        c_h3=abs(h3-h)
        if (c_h2<=c_h1) & (c_h2<=c_h3):
            return x, y + 1, c_h2
        elif (c_h1<c_h2) & (c_h3<c_h2) & (c_h1==c_h3):
            return x+1,y+1,c_h3
        else:
            smallest=min(c_h1,c_h2,c_h3)
            if smallest==c_h1:
                return x-1, y + 1, c_h1
            elif smallest==c_h2:
                return x, y + 1, c_h2
            else:
                return x+1, y+1,c_h3

#read data
data=sys.stdin.readlines()
size=list(map(int,data[0].split()))
start=list(map(int,data[1].split()))
map=[]
for line in data[2:]:
    line=line.split()
    row=[int(i) for i in line]
    #row=list(map(int, line.split()))
    map.append(row)

#start travelling
current_x=start[0]
current_y=start[1]
total_dis=0

while current_y<size[1]-1:
    current_x,current_y,dis= make_decision(current_x,current_y,map[current_x][current_y])
    total_dis+=dis

print(current_x,current_y,total_dis)