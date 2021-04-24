k=[int(i) for i in input().split()]
span=[None]*len(k)
stack=[]
for i in range(len(k)):
    if(i==0):
        stack.append(i)
        span[i]=1
    else:
        while stack and k[stack[-1]]<k[i]:
            stack.pop()
        if(not stack):
            span[i]=i+1
        else:
            span[i]=i-stack[-1]
        stack.append(i)
print(span)