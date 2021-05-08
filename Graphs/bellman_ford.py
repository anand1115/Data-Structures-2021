class Graph:
    def __init__(self,edges,vertices):
        self.edges=edges
        self.vertices=vertices
        self.graph_dict={}
        for i,j,v in edges:
            if i in self.graph_dict:
                self.graph_dict[i][j]=v
            else:
                self.graph_dict[i]={j:v}

    def print(self):
        for i in self.graph_dict:
            print(i,"-->",self.graph_dict[i])

    def shortest_path(self,source):
        distance={i:float("inf") for i in vertices}
        distance[source]=0
        for i in range(len(self.vertices)-1):
            for a,b,c in self.edges:
                if distance[b]>distance[a]+self.graph_dict[a][b]:
                    distance[b]=distance[a]+self.graph_dict[a][b]
        for i,j,v in self.edges:
            if(distance[j]>distance[i]+self.graph_dict[i][j]):
                print("Distance Can't be created due to negative cycle")
                return
        print(distance)
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
vertices=["A","B","C","D","E"]
g=Graph(edges,vertices)
g.print()
g.shortest_path("A")
