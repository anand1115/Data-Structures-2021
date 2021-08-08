def graph(nodes,k,n):
    temp=[]
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if(abs(i-j)<=k and nodes[i]>nodes[j]):
                temp.append((i,j,1))
    return temp
def floyd_warshall(n,edges):
    distance={i:{j:float("inf") if i!=j else 0  for j in range(n)} for i in range(n)}
    for i,j,v in edges:
        distance[i][j]=v
    for i in range(n):
        for j in range(n):
            for k in range(n):
                distance[j][k]=min(distance[j][k],distance[j][i]+distance[i][k])
    return distance 

n=int(input())
k=int(input())
mx=0
nodes=[]
for i in range(n):
    t=int(input())
    nodes.append(t)
    if(t>mx):
        mx=t
prime=[True]*(mx+1)
prime[0]=False
prime[1]=False
p=2
while(p*p<=mx):
    for i in range(p*2,mx+1,p):
        prime[i]=False
    p+=1
primes=[]
for i in range(n):
    if(prime[nodes[i]]):
        primes.append(i)
graph=graph(nodes,k,n)
final=floyd_warshall(n,graph)
ans=0
for i in range(n):
    temp=0
    if(prime[nodes[i]]):
        continue
    else:
        for j in primes:
            if(final[i][j] == float('inf')):
                continue
            else:
                if(final[i][j]>temp):
                    temp=final[i][j]
    ans+=temp
print(ans)
                
            

