class graph:
    def __init__(self,edges,vertices):
        self.edges=edges
        self.vertices=vertices
        self.graph_dict={}
        for i,j in edges:
            if i in self.graph_dict:
                self.graph_dict[i].append(j)
            else:
                self.graph_dict[i]=[j]

    def Breadth_First_Search(self):
        queue=[]
        visited={i:False for i in self.vertices}
        output=[]
        queue.append(self.vertices[0])
        visited[self.vertices[0]]=True
        while queue:
            v=queue.pop()
            output.append(v)
            try:
                for i in self.graph_dict[v]:
                    if not visited[i]:
                        queue.insert(0,i)
                        visited[i]=True
            except:
                pass
        return output

    def Depth_First_Search(self):
        stack=[]
        visited={i:False for i in self.vertices}
        output=[]
        stack.append(self.vertices[0])
        visited[self.vertices[0]]=True
        while stack:
            v=stack.pop()
            output.append(v)
            try:
                for i in self.graph_dict[v]:
                    if not visited[i]:
                        stack.append(i)
                        visited[i]=True
            except:
                pass
        return output
edges=[
    (0,1),
    (0,1),
    (1,2),
    (2,0),
    (2,3),
    (3,3)
    ]
vertices=[0,1,2,3]
k=graph(edges,vertices)
print(k.Breadth_First_Search())
print(k.Depth_First_Search())
            
                    
