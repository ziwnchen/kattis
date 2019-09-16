import sys

def find_rep(string,j):
    ch=string[j]
    while (string[j]==ch):
        j+=1
        if j==len(name):
            break
    return j-1

name=sys.stdin.readline().strip()
new_name=""
i=0

while i<=len(name)-1:
    new_name+=name[i]
    num=find_rep(name,i)
    if num==i:
        i+=1
    else:
        i=num+1

print(new_name)