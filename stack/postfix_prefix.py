#postfix --->prefix======>postfix->infix->prefix
#postfix-->infix
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
    infix=stack.pop()
infix=list(infix[::-1])
for i,v in enumerate(infix):
    if(v=='('):
        infix[i]=")"
    elif(v==")"):
        infix[i]="("



stack=[]
operators={"(":0,'+':1,"-":1,"*":2,"/":2,"^":3}
op=[]
for i in infix:
    if(i.isalpha() or i.isnumeric()):
        op.append(i)
    elif i=="(":
        stack.append(i)
    elif(i==")"):
        while stack and stack[-1]!='(':
            op.append(stack.pop())
        stack.pop()
    else:
        while stack and operators[stack[-1]]>operators[i]:
            op.append(stack.pop())
        stack.append(i)
while stack:
    
    op.append(stack.pop())
prefix="".join(op[::-1])
print(prefix)



