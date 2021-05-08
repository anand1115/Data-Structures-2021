class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for i,v in self.edges:
            if i in self.graph_dict:
                self.graph_dict[i].append(v)
            else:
                self.graph_dict[i]=[v]

    def print_graph(self):
        for i in self.graph_dict:
            print(i,"-->",*self.graph_dict[i],sep=" ")
    
    def bfs_traversal(self):
        q=["A"]
        visited=["A"]
        while len(q)!=0:
            v=q.pop()
            print(v,end=" ")
            try:
                for i in self.graph_dict[v]:
                    if(i not in visited):
                        visited.append(i)
                        q.insert(0,i)
            except:
                pass
    def dfs_traversal(self):
        stack=["A"]
        visited=["A"]
        while len(stack)!=0:
            v=stack.pop()
            print(v,end=" ")
            try:
                for i in self.graph_dict[v]:
                    if i not in visited:
                        stack.append(i)
                        visited.append(i)
            except:
                pass
edges=[
        ("A","B"),
        ("A","C"),
        ("A","D"),
        ("C","E"),
        ("C","F"),
        ("D","F"),        
        ]
graph=Graph(edges)
graph.bfs_traversal()
print("\n")
graph.dfs_traversal()
            
        
