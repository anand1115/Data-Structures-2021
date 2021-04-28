cost=[0,1,2,3,5,6,8,9]
n=int(input())
rod=[0]*(n+1)
rod[0]=0
for i in range(1,n+1):
    mx=0
    for j in range(1,i+1):
        mx=max(mx,cost[j]+rod[j])
    rod[i]=mx
print(rod)