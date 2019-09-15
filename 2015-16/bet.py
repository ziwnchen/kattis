import sys

data=sys.stdin.readlines()
m1=float(data[0])#could be float
b1=float(data[1])
n=int(data[2])
results=list(map(int, data[3].split()))


m_current=m1
b_current=b1

for i in range(n):
    result=results[i]
    if result==0:
        #tail
        m_current=m_current-b_current
        b_current=min(2*b_current,m_current)
    else:
        m_current=m_current+b_current
        b_current=min(b1,m_current)
    if m_current <= 0:
        break

if m_current<=0:
    print("BROKE")
else:
    print(int(m_current))