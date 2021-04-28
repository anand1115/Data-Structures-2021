n=int(input())
fact=[0]*(n+1)
fact[0]=1
fact[1]=1
for i in range(2,n+1):
    fact[i]=i*fact[i-1]
print(fact)
print(fact[n])