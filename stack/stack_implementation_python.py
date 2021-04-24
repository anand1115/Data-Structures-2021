class stack:
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return self.items==[]

    def peek(self):
        if(self.is_empty()):
            raise ValueError("UnderFlow Error.Stack is empty!!!!")
        else:
            return self.items[-1]
        
    def pop(self):
        if(self.is_empty()):
            raise ValueError("UnderFlow Error.Stack is Empty!!!")
        else:
            return self.items.pop()
    
    def push(self,data):
        self.items.append(data)
    
    def print(self):
        if(self.is_empty()):
            print("Empty Stack")
            return 
        print(*self.items,sep="\n")
stack=stack()
stack.push(10)
stack.push(20)
stack.push(40)
stack.push(30)
stack.print()
print("*"*15)
stack.pop()
stack.pop()
stack.pop()
stack.print()
print(stack.is_empty())
print(stack.peek())
