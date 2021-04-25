n=list(map(int,input().split()))
nq=int(input())
s=[]
for i in range(nq):
    s.append(list(map(int,input().split())))
span=[0]*n[0]
for i in s:
    span[i[0]]+=i[2]
    if(i[1]<(n[0]-1)):
        span[i[1]+1]-=i[2]
    elif(i[1]==n[0]-1):
        pass
for i in range(len(span)):
    if(i==0):
        pass
    else:
        span[i]+=span[i-1]
print(*[sum(i) for i in zip(n[1:],span)],sep=" ")
    
    





