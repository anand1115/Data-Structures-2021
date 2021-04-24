k=input()
operators={'(':0,'+':1,'-':1,'*':2,'/':2,'%':2,'^':3}
stack=[]
op=[]
for i in k:
    if(i.isalpha() or i.isalnum()):
        op.append(i)
    elif(i=="("):
        stack.append(i)
    elif(i==')'):
        while stack and stack[-1]!="(":
            op.append(stack.pop())
        stack.pop()     
    else:
        while stack and operators[stack[-1]]>=operators[i]: #here is the change for infix to prefix
            op.append(stack.pop())
        stack.append(i)
while stack:
    op.append(stack.pop())
print(k,"".join(op),sep="\n")