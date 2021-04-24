k=list(map(int,input().split()))
stack=[]
count={i:k.count(i) for i in set(k)}
op=[None]*len(k)
for i in range(len(k)):
    if(i==0):
        stack.append(i)
    else:
        while(stack and count[k[stack[-1]]]<count[k[i]]):
            s=stack.pop()
            op[s]=k[i]
        stack.append(i)
while stack:
    op[stack.pop()]=-1
print(op)
