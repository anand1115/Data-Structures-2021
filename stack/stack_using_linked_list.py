class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.head=None
    
    def is_empty(self):
        if(self.head is None):
            return True
        else:
            return False
    
    def peek(self):
        if(self.is_empty()):
            raise ValueError("UnderFlow Error.Stack is empty!!!")
        else:
            return self.head.data
    
    def push(self,data):
        new_node=Node(data)
        if(self.is_empty()):
            self.head=new_node
        else:
            temp=self.head
            self.head=new_node
            new_node.next=temp
    def pop(self):
        if(self.is_empty()):
            raise ValueError("UnderFlow Error.stack is empty")
        else:
            data=self.head.data
            self.head=self.head.next
            return data
    def print(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next


k=stack()
k.push(10)
k.print()
k.push(20)
k.push(80)
k.push(30)
k.push(50)
k.push(60)
print("*"*10)
k.print()
k.pop()
k.pop()
print("*"*10)
k.print()

