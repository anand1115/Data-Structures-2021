k=input()[::-1]
stack=[]
for i in k:
    if(i.isalpha() or i.isnumeric()):
        stack.append(i)
    else:
        a=stack.pop()
        b=stack.pop()
        exp="("+a+i+b+")" #change in postifix conversion*+AB-CD
        stack.append(exp)
if(len(stack)==1):
    print(stack.pop())
