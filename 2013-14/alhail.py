import sys

data=sys.stdin.readline().strip()
new_name=""
i=0
def switch(a,b):
    return str(b)+str(a)

if len(data)%2==0:
    while i<len(data)-1:
        part=switch(data[i],data[i+1])
        new_name+=part
        i+=2
else:
    while i<len(data)-2:
        part=switch(data[i],data[i+1])
        new_name+=part
        i+=2
    new_name+=data[-1]

print(new_name)