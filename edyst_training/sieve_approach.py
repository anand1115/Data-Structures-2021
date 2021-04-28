mx=int(input())
prime=[True]*(mx+1)
prime[0]=False
prime[1]=False
p=2
while(p*p<=mx):
    for i in range(p*2,mx+1,p):
        prime[i]=False
    p+=1
for i,v in enumerate(prime):
    if(v):
        print(i)


    






