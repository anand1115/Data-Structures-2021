def count(n):
    c=0
    while n>0:
        sum=n&1
        if(sum==1):
            c+=1
        n=n>>1
    return c
def check(num):
    if(num<0):
        return False
    if(count(num)==1):
        return True
    else:
        return False
k=int(input())
print(check(k)) 

