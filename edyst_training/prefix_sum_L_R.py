n=int(input("Enter the length of array"))
k2=list(map(int,input("Enter the list elements separated by spaces :").split()))
s=[None]*n
qn=int(input("Enter Number of queries :"))
q_list=[]
l=[]
r=[]
for i in range(qn):
    k=list(map(int,input("Enter query-{}".format(i)).split()))
    l.append(k[0])
    r.append(k[1])
    q_list.append(k)

for i in range(n):
    if(i==0):
        s[i]=k2[i]
    else:
        s[i]=s[i-1]+k2[i]

for l,r in q_list:
    if(l==0):
        t=s[r]
    else:
        t=s[r]-s[l-1]
    print("{}-{}={}".format(l,r,t))

