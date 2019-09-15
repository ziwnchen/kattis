import sys
import itertools

#read file
data=sys.stdin.readlines()
N=int(data[0])
location={}

for i in range(N):
    coord = list(map(int, data[i+1].split()))
    x=coord[0]
    y=coord[1]
    location[i]=(x,y)

#make judgement
status=1
queens=list(location.keys())
pairs=list(itertools.combinations(queens,2))
for pair in pairs:
    q1=location[pair[0]]
    q2=location[pair[1]]
    #column
    if q1[0]==q2[0]:
        status=0
        break
    #row
    if q1[1]==q2[1]:
        status=0
        break
    #diagonal
    k=abs((q1[1]-q2[1])/(q1[0]-q2[0]))
    if k==1:
        status=0
        break

#return
if status==1:
    print("CORRECT")
else:
    print("INCORRECT")