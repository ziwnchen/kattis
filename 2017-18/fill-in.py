def fill(a,i,x):
    a[i]=x

def rec_fill(a,N,i,x):
    #forward loop
    start=i
    if i<0 or i>=N:
        return
    else:
        v=a[i]
    while a[i]!=x:
        fill(a,i,x)
        i=i+1
        if i>=N or a[i]!=v:
            break
    #backward loop
    i=start-1
    if i<0 or i>=N:
        return
    else:
        while a[i]!=x:
            if a[i]!=v:
                break
            else:
                fill(a,i,x)
                i=i-1
                if i<0:
                    break

#main fuction here
import sys
import os

file_path= os.path.dirname(__file__)
script=os.path.join(file_path, 'fill_in.py')
print(file_path)
print(script)
"/home/ziwenchen/dis_cal/shortest_dis_spark.py"