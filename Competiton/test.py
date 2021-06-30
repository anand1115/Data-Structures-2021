from collections import defaultdict
import heapq
def make_adj_list(vertices,edges,c):
    final=defaultdict(list)
    for i,j in edges:
        if (j,c) not in final[i]:
            final[i].append((j,c))
        if (i,c) not in final[j]:
            final[j].append((i,c))
    return final
def shortest_distance(vertices,edges,adj_list,t):
    distance={i:float("infinity") for i in vertices}
    queue=[(0,1)]
    distance[1]=0
    while queue:
        current_distance,current_vertex=heapq.heappop(queue)
        if(current_distance>=t):
            current_distance+=(t-(current_distance%t))
        if(current_distance<distance[current_vertex]):
            continue
        if not adj_list.get(current_vertex):
            continue
        for i,j in adj_list[current_vertex]:
            dist=current_distance+j
            if(dist<distance[i]):
                distance[i]=dist
                heapq.heappush(queue,(dist,i))
    return distance
n,m,t,c=list(map(int,input().split()))
vertices=[i+1 for i in range(n)]
edges=[]
for i in range(m):
    edges.append(tuple(map(int,input().split())))
adj_list=make_adj_list(vertices,edges,c)
short=shortest_distance(vertices,edges,adj_list,t)
print(short[n])
