import sys

data=sys.stdin.readline().split()
x=int(data[0])
n=int(data[1])

def exp(x,n):
    if n==0:
        return 1
    elif n==1:
        return x
    elif (n>1) & (n%2==0):
        return exp(x*x,n/2)
    elif (n>1) & (n%2==1):
        return exp(x*x,(n-1)/2)*x

print(exp(x,n))