import sys

#DFS
def dfs(root):
    root_pos=vertice.index(root)
    visit[root_pos]=1
    for k in edges_dict[root]:
        pos=vertice.index(k)
        if visit[pos]==0:
            visit[pos]=1
            dfs(k)

data=sys.stdin.readlines()
v=int(data[0])
e=int(data[1])

vertice=list(range(v))
visit=[0]*v
edges_dict={j:[] for j in vertice}

#save as dict of list
for i in data[2:]:
    points=i.split()
    edges_dict[int(points[0])].append(int(points[1]))
    edges_dict[int(points[1])].append(int(points[0]))

#start searching
search_time=0
while (0 in visit):
    z_pos=visit.index(0)
    dfs(z_pos)
    search_time+=1

print(search_time)











