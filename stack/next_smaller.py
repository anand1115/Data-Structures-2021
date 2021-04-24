k=list(map(int,input().split()))
stack=[]
op=[None]*len(k)
for i in range(len(k)):
    if(i==1):
        stack.append(i)
    else:
        while stack and k[stack[-1]]>k[i]:
            s=stack.pop()
            op[s]=k[i]
        stack.append(i)
while stack:
    op[stack.pop()]=-1
print(op)