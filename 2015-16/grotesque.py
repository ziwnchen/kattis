import sys

data=sys.stdin.readline()
spots=list(map(int,data.split()))

sum=0
sp=False
for i in spots:
    if i<6:
        sum=sum+i
    else:
       sp=True
       break

if sp:
    print("CLEAN")
elif sum>=30:
    print("CLEAN")
else:
    print("DO NOT CLEAN")