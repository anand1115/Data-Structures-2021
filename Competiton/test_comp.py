from collections import defaultdict,deque
def make_list(edges,vertices):
    final=defaultdict(list)
    for i,j in edges:
        final[i].append(j)
    for i in vertices:
        if i not in final:
            final[i]=[]
    return final
def check(vertices,adj_list,source,destination):
    visited={i:False for i in vertices}
    queue=deque()
    queue.appendleft(source)
    visited[source]=True
    while queue:
        temp=queue.pop()
        if(temp==destination):
            return 1
        for i in adj_list[temp]:
            if not visited[i]:
                visited[i]=True
                queue.appendleft(i)
    return 0
    
n=int(input())
vertices=[int(input()) for i in range(n)]
m=int(input())
edges=[tuple(map(int,input().split())) for i in range(m)]
s=int(input())
d=int(input())
adj_list=make_list(edges,vertices)
print(check(vertices,adj_list,s,d))
    


from collections import defaultdict,deque
import heapq
def make_list(edges,vertices):
    final=defaultdict(list)
    for i,j,t in edges:
        final[i].append((j,t))
    for i in vertices:
        if i not in final:
            final[i]=[]
    return final
def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0
    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances
n=int(input())
vertices=[int(input()) for i in range(n)]
m=int(input())
edges=[tuple(map(int,input().split())) for i in range(m)]
s=int(input())
d=int(input())
adj_list=make_list(edges,vertices) 
k=calculate_distances(adj_list,s)
print(k[d])

    



def get_mat(vertices,edges):
    mat=[[0 for j in range(len(vertices))] for i in range(len(vertices))]
    for i,j in edges:
        mat[i][j]=1
    return mat


from collections import defaultdict

class Graph:
    def __init__(self,graph):
        self.graph = graph
        self.org_graph = [i[:] for i in graph]
        self. ROW = len(graph)
        self.COL = len(graph[0])

    def BFS(self,s, t, parent):
        visited =[False]*(self.ROW)
        queue=[]
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0 :
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return True if visited[t] else False
		
    def dfs(self, graph,s,visited):
        visited[s]=True
        for i in range(len(graph)):
            if graph[s][i]>0 and not visited[i]:
                self.dfs(graph,i,visited)

    def minCut(self, source, sink,rev):
        parent = [-1]*(self.ROW)
        max_flow = 0
        while self.BFS(source, sink, parent) :
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        visited=len(self.graph)*[False]
        self.dfs(self.graph,s,visited)
        final=set()
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.graph[i][j] == 0 and self.org_graph[i][j] > 0 and visited[i]:
                    if j!=sink:
                        final.add(rev[i])
                        final.add(rev[j])
        return final
n=int(input())
vertices={int(input()):i for i in range(n)}
rev={vertices[i]:i for i in vertices}
m=int(input())
edges=[list(map(int,input().split())) for i in range(m)]
for i in edges:
    i[0]=vertices[i[0]]
    i[1]=vertices[i[1]]    
s=int(input())
d=int(input())
k=get_mat(vertices,edges)
g=Graph(k)
source=vertices[s]
sink=vertices[d]
out=g.minCut(source, sink,rev)
print(*list(out))






