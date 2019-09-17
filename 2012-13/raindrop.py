import sys

data=sys.stdin.readlines()
n=int(data[0])
mea=list(map(int, data[1].split()))

ifpos=False

new_mea=[]
for i in mea:
    if i<0:
        continue
    else:
        new_mea.append(i)
        ifpos=True

if ifpos:
    print(int(sum(new_mea)/len(new_mea))
























          )





















else:
    print("INSUFFICIENT DATA")