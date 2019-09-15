import sys

data=sys.stdin.readlines()
np=int(data[0])
bases=list(map(int,data[1].split()))

walk_count=0
sum=0
#count the number of walk
for i in bases:
    if i==-1:
        walk_count=walk_count+1
    sum=sum+i

slug_avg= float((sum+walk_count)/(np-walk_count))
print(slug_avg)

