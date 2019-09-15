import sys

data=sys.stdin.readlines()
community=data[0].strip()
number=int(data[1])
names=[]
for i in data[2:]:
    names.append(i.strip())
n_princess=0
n_baron=0
n_priest=0
n_common=0



for p in names:
    if community in p:
        pos=p.index(community)
        if pos==0:
            n_princess+=1
        elif pos==(len(p)-len(community)):
            n_baron+=1
        else:
            n_priest+=1
    else:
        n_common+=1

print(str(n_princess)+" PRINCESS\n"+str(n_baron)+" BARON\n"+str(n_priest)+" PRIEST\n"+str(n_common)+" COMMONER")