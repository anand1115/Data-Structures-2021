k=[11,23,10,37,21,50,80]
n=len(k)
l=[1]*n
for i in range(1,n):
    for j in range(i):
        if(k[i]>k[j] and l[i]<l[j]+1):
            l[i]=l[j]+1
print(max(l))