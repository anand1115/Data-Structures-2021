class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for start,end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        print(self.graph_dict)


    def get_paths(self,start,end,path=[]):
        path=path+[start]
        if(start==end):
            return [path]
        if(start not in self.graph_dict):
            return []
        paths=[]
        for node in self.graph_dict[start]:
            if node not in path:
                new_path=self.get_paths(node,end,path)
                for p in new_path:
                    paths.append(p)
        return paths
            
            

paths=[
    ("mumbai","paris"),
    ("mumbai","dubai"),
    ("paris","dubai"),
    ("paris","newyork"),
    ("dubai","newyork"),
    ("newyork","toronto"),   
    ]
graph=Graph(paths)
print(graph.get_paths("mumbai","newyork"))
                
