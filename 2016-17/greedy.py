import sys

def make_decision(x,y,h):
    if (x==0) & (x!=(size[0]-1)):
        h2=hike_map[x][y+1]
        h3=hike_map[x+1][y+1]
        c_h2=abs(h2-h)
        c_h3=abs(h3-h)
        if c_h2<=c_h3:
            return x,y+1,c_h2
        else:
            return x+1,y+1,c_h3
    elif (x==(size[0]-1)) & (x!=0):
        h1=hike_map[x-1][y+1]
        h2=hike_map[x][y+1]
        c_h2=abs(h2-h)
        c_h1=abs(h1-h)
        if c_h2<=c_h1:
            return x,y+1,c_h2
        else:
            return x-1,y+1,c_h1
    elif (x==(size[0]-1)) & (x==0):
        h2=hike_map[x][y+1]
        c_h2 = abs(h2 - h)
        return x,y+1,c_h2
    else:
        h1=hike_map[x-1][y+1]
        h2=hike_map[x][y+1]
        h3=hike_map[x+1][y+1]
        c_h1=abs(h1-h)
        c_h2=abs(h2-h)
        c_h3=abs(h3-h)
        #smallest=min(c_h1,c_h2,c_h3)
        if (c_h3<c_h2) & (c_h3<=c_h1):
            return x+1, y + 1, c_h3
        elif c_h1<c_h2:
            return x-1, y + 1, c_h1
        else:
            return x, y+1,c_h2

#read data
data=sys.stdin.readlines()
size=list(map(int,data[0].split()))
start=list(map(int,data[1].split()))
hike_map=[]
for line in data[2:]:
    line=line.split()
    row=[int(i) for i in line]
    hike_map.append(row)

#start travelling
current_x=start[0]
current_y=start[1]
total_dis=0

while current_y<size[1]-1:
    current_x,current_y,dis= make_decision(current_x,current_y,hike_map[current_x][current_y])
    total_dis+=dis

print(current_x,current_y,total_dis)