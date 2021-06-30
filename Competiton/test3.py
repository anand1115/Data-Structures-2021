from collections import defaultdict
def get_adj_list(edges,c):
    final=defaultdict(list)
    for i,j in edges:
        if (i,c) not in final[j]:
            final[j].append((i,c))
        if (j,c) not in final[i]:
            final[i].append((j,c))
    return final
paths=[]
def get_all_paths(u,d,visited,list,path=[]):
    visited[u]=True
    path.append(u)
    if(u==d):
        paths.append(tuple(path))
    else:
        for i,w in list[u]:
            if visited[i]==False:
                get_all_paths(i,d,visited,list,path)
    path.pop()
    visited[u]=False
            
n,m,t,c=list(map(int,input().split()))
vertices=[i+1 for i in range(n)]
edges=[]
for i in range(m):
    edges.append(tuple(map(int,input().split())))
k=get_adj_list(edges,c)
visited={i+1:False for i in range(n)}
get_all_paths(1,n,visited,k)
paths=sorted(paths,key=len)
f={i:0 for i in vertices}
for i in paths:
    for j in i:
        f[j]=1
for i in f:
    print(f[i],end=" ")
    

            
        
    


