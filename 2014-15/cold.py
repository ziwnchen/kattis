import sys

data=sys.stdin.readlines()
n=int(data[0])
weathers=list(map(int, data[1].split()))
sum=0
for i in weathers:
    if i<0:
        sum+=1
print(sum)