import sys

data=sys.stdin.readlines()
n=int(data[0])
meas=list(map(int, data[1].split()))

meas.sort()

print(abs(meas[-1]-meas[0]))