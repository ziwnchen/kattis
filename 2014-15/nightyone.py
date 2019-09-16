import sys

data=sys.stdin.readline()
number=int(data)

def M(n):
    if n>100:
        return n-10
    else:
        return M(M(n+11))

print(M(number))