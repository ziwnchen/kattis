import sys

data=sys.stdin.readline().split()
x=int(data[0])
y=int(data[1])

def gcd(a,b):
    if a==b:
        return a
    elif a>b:
        return gcd(a-b,b)
    else:
        return gcd(a,b-a)

print(gcd(x,y))