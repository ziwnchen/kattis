import sys
import math

data=sys.stdin.readlines()
para=data[0].split()
N=int(para[0])
M=int(para[1])

max=0

students=[]
grades_list=[]

for i in range(N):
    info=data[i+1].split()
    name=info[0]
    final=int(info[M+1])
    grades=list(map(int,info[1:M+1]))
    grades.sort()
    grades.remove(grades[0])
    score=sum(grades)+final
    if score>max:
        max=score
    students.append(name)
    grades_list.append(score)

for j in range(N):
    student=students[j]
    if max!=0:            
        total=grades_list[j]
        raw=float(100*total/max)
        ad_score=int(math.ceil(raw))
    else:
        total = grades_list[j]
        ad_score=0

    if ad_score>=90 and ad_score<=100:
        letter='A'
    elif ad_score>=80 and ad_score<90:
        letter='B'
    elif ad_score>=70 and ad_score<80:
        letter='C'
    elif ad_score>=60 and ad_score<70:
        letter='D'
    elif ad_score<60:
        letter='F'
    print(student+" "+str(int(total))+" "+str(ad_score)+" "+letter)







