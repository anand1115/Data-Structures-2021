from collections import deque
class Graph:
    def __init__(self,edges,vertices):
        self.edges=edges
        self.vertices=vertices
        self.graph_dict={}
        for i,j in edges:
            if i in self.graph_dict:
                self.graph_dict[i].append(j)
            else:
                self.graph_dict[i]=[j]
    

    def print_graph(self):
        for i in self.graph_dict:
            print(i,"-->",*self.graph_dict[i],sep=" ")
    

    def bfs_traversal(self):
        queue=deque()
        visited={i:False for i in self.vertices}
        queue.appendleft("A")
        visited["A"]=True
        while len(queue)!=0:
            v=queue.pop()
            print(v,end=" ")
            try:
                for i in self.graph_dict[v]:
                    if not visited[i]:
                        queue.appendleft(i)
                        visited[i]=True
            except:
                pass

    def dfs_traversal(self):
        stack=[]
        visited={i:False for i in self.vertices}
        stack.append("A")
        visited["A"]=True
        while len(stack)!=0:
            v=stack.pop()
            print(v,end=" ")
            try:
                for i in self.graph_dict[v]:
                    if not visited[i]:
                        stack.append(i)
                        visited[i]=True
            except:
                pass
            
                
            


edges=[
    ("A","B"),
    ("A","D"),
    ("B","A"),
    ("B","C"),
    ("C","B"),
    ("C","D"),
    ("C","G"),
    ("D","A"),
    ("D","C"),
    ("D","E"),
    ("E","D"),
    ("E","F"),
    ("F","G"),
    ("F","E"),
    ("G","C"),
    ("G","F"),
    ]
vertices=["A","B","C","D","E","F","G"]
graph=Graph(edges,vertices)
graph.print_graph()
graph.bfs_traversal()
print("\n")
graph.dfs_traversal()
