import sys

data=sys.stdin.readlines()
N=int(data[0])

num_a=0
num_c=0
num_g=0
num_t=0

for i in range(N):
    #scan each line
    string=data[i+1]
    a=string.count('A')
    c=string.count('C')
    g=string.count('G')
    t=string.count('T')
    num_a=num_a+a
    num_c=num_c+c
    num_g+=g
    num_t+=t

ratio=float(num_c+num_g)/float(num_c+num_g+num_a+num_t)
print(ratio*100)
