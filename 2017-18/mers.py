import sys

data=sys.stdin.readlines()
para=list(map(int, data[0].split()))
L=int(para[0])
N=int(para[1])
k=int(para[2])
Q=int(para[3])
string=data[1:L+1]
kmers=data[L+1:]

new_string=""
for i in range(L):
    new_string=new_string+data[i+1].strip()

mer_dict={}

#scan for mers
for j in range(N-k+1):
    current_mer=""
    for m in range(k):
        current_mer=current_mer+new_string[j+m]
    if current_mer in mer_dict.keys():
        freq=mer_dict[current_mer]
        mer_dict[current_mer]=freq+1
    else:
        mer_dict[current_mer]=1

#print out mer number
for mer in kmers:
    if mer.strip() in mer_dict.keys():
        print(mer.strip()+" "+str(mer_dict[mer.strip()]))
    else:
        print(mer.strip()+" 0")