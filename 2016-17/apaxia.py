import sys

data=sys.stdin.readline()
first=data.split()[0]
last=data.split()[1]

len_last=len(last)
if len_last==5:
    new_last=last*4
else:
    new_last=last*len_last

print(first+" "+new_last)