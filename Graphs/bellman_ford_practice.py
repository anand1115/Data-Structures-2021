class graph:
    def __init__(self,edges,vertices):
        self.edges=edges
        self.vertices=vertices
        self.graph_dict={}
        for i,j,v in self.edges:
            if i in self.graph_dict:
                self.graph_dict[i][j]=v
            else:
                self.graph_dict[i]={j:v}

    def print(self):
        for i in self.graph_dict:
            print(i,"-->",self.graph_dict[i])

    def shortest_path(self,source):
        distance={i:float("inf") for i in self.vertices}
        distance[source]=0
        for i in range(len(self.vertices)-1):
           for i,j,v in self.edges:
               if(distance[j]>distance[i]+self.graph_dict[i][j]):
                   distance[j]=distance[i]+self.graph_dict[i][j]
        print(distance)

    def floyd_warshall(self):
        distance={i:{j:float("inf") if i!=j else 0  for j in self.vertices} for i in self.vertices}
        for i,j,v in self.edges:
            distance[i][j]=v
        for i in self.vertices:
            for j in self.vertices:
                for k in self.vertices:
                    distance[j][k]=min(distance[j][k],distance[j][i]+distance[i][k])
        for i in distance:
            print(i,distance[i])

    def count_in_degree(self):
        count={i:0 for i in self.vertices}
        for i,j,v in self.edges:
            if(j in count):
                count[j]+=1
        return count
        

    def tropological_sort(self):
        count=self.count_in_degree()
        queue=[]
        out=[]
        for i in count:
            if count[i]==0:
                queue.insert(0,i)
        while queue:
            v=queue.pop()
            out.append(v)
            try:
                for i in self.graph_dict[v]:
                    count[i]-=1
                    if(count[i]==0):
                        queue.insert(0,i)
            except:
                pass
        if(len(count)!=len(out)):
            print("Topological Sort Won't work.")
        else:
            print(*out)

edges=[
    ("A","B",4),
    ("A","C",2),
    ("B","C",3),
    ("B","D",2),
    ("B","E",3),
    ("C","B",1),
    ("C","D",4),
    ("C","E",5),
    ("E","D",-5),
    ]
vertices="ABCDE"
k=graph(edges,vertices)
k.print()
k.shortest_path("A")
k.floyd_warshall()
edges=[
    (0,1,3),
    (0,4,-4),
    (0,2,8),
    (1,3,1),
    (1,4,7),
    (2,1,4),
    (3,0,2),
    (3,2,-5),
    (4,3,6),    
    ]
vertices=[0,1,2,3,4]
k=graph(edges,vertices)
k.floyd_warshall()
edges=[
    [0,1,0],
    [0,2,0],
    [1,2,0],
    [1,3,0],
    [2,3,0],
    [2,4,0]
    ]
vertices=[0,1,2,3,4]
k=graph(edges,vertices)
k.tropological_sort()
