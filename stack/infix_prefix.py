k=input()
operators={'(':0,'+':1,'-':1,'*':2,'/':2,'^':3}
k=list(k[::-1])
for i in range(len(k)):
    if(k[i]=='('):
        k[i]=')'
    elif(k[i]==')'):
        k[i]='('
k="".join(k)
op=[]
stack=[]
for i in k:
    if(i.isalpha() or i.isnumeric()):
        op.append(i)
    elif(i=='('):
        stack.append(i)
    elif(i==')'):
        while stack and stack[-1]!='(':  
            op.append(stack.pop())
        stack.pop()
    else:
        while stack and operators[stack[-1]]>operators[i]: #here is the change for infix to postfix
            op.append(stack.pop())
        stack.append(i)
while stack:
    op.append(stack.pop())
print(k,"".join(op[::-1]),sep="\n")

