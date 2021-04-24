k=input()
stack=[]
for i in k:
    if(i.isalpha() or i.isnumeric()):
        stack.append(i)
    else:
        a=stack.pop()
        b=stack.pop()
        exp="("+b+i+a+")"
        stack.append(exp)
if(len(stack)==1):
    print(stack.pop())