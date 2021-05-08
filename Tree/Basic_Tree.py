class Tree:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    

    def addchild(self,data):
        k=Tree(data)
        k.parent=self
        self.children.append(k)
        print("Node Added")
    
    def get_level(self):
        c=1
        k=self.parent
        while k:
            c=c+1
            k=self.parent.parent
        return c
    
    def print_tree(self):
        print(self.data)
        for i in self.children:
            i.print_tree()

electronics=Tree("Electronics")
lap=electronics.addchild("Laptops")
lap.addchild("MacBook")
lap.addchild("EliteBook")
lap.addchild("Microsoft")
cell=electronics.addchild("Cell Phones")
cell.addchild("Iphone")
cell.addchild("Google")
cell.addchild("Vivo")
tel=electronics.addchild("Telivisions")
tel.addchild("Samsung")
tel.addchild("Lg")
tel.addchild("Onida")


