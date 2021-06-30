def adj_list(vertices,edges,c):
    k={}
    for i,v in edges:
        if i in k:
            k[i].add((v,c))
        else:
            k[i]={(v,c)}
        if v in k:
            k[v].add((i,c))
        else:
            k[v]={(i,c)}
    for i in k:
        k[i]=list(k[i])
    return k
import heapq
def make_distance(vertices,list,start,t):
    distance={i:float('infinity') for i in vertices}
    distance[start]=0
    queue=[(0,start)]
    while queue:
        current_distance,current_index=heapq.heappop(queue)
        if(current_distance>t):
            current_distance+=3-(current_distance%3)
        if(current_distance<distance[current_index]):
            continue
        if not list.get(current_index):
            continue
        for j,w in list[current_index]:
            dist=current_distance+w
            if(dist<distance[j]):
                distance[j]=dist
                heapq.heappush(queue,(dist,j))
    return distance
n,m,t,c=list(map(int,input().split()))
edges=[]
vertices=[i+1 for i in range(n)]
for i in range(m):
    edges.append(list(map(int,input().split())))
k=adj_list(vertices,edges,c)
print(make_distance(vertices,k,1,t))


    
