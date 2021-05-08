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
            print(i,"==>",self.graph_dict[i],sep=" ")
            
