import sys

name=sys.stdin.readline().strip()

first=name[0]
sum=0

for i in name:
    if i==first:
        sum+=1

print(sum)