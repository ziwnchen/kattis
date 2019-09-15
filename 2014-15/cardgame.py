import sys

data=sys.stdin.readlines()
n=int(data[0])
p1=data[1].split()
p2=data[2].split()

#change from character to number

def change(p):
    p_new=[0]*n
    for i in range(n):
        if p[i]=='J':
            p_new[i]=11
        elif p[i]=='Q':
            p_new[i]=12
        elif p[i]=='K':
            p_new[i]=13
        elif p[i]=='A':
            p_new[i]=20
        else:
            p_new[i]=int(p[i])
    return p_new

p1=change(p1)
p2=change(p2)
p1_score=0
p2_score=0
#competition
for i in range(n):
    first=p1[i]
    second=p2[i]
    if first==second:
        continue
    elif first>second:
        p1_score+=1
    else:
        p2_score+=1

if p1_score==p2_score:
    print('TIE')
elif p1_score>p2_score:
    print('PLAYER 1 WINS')
else:
    print('PLAYER 2 WINS')