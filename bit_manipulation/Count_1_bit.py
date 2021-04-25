def count(n):
    c=0
    while n>0:
        sum=n&1
        if(sum==1):
            c+=1
        n=n>>1
    return c
def count_method2(n):
    c=0
    while n>0:
        c+=1
        n=n&(n-1)
    return c
n=int(input())
print(count(n),count_method2(n))