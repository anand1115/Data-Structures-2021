n=int(input())
bags=list(map(float,input().split()))
bags.sort()
a=bags
c=0
while bags:
    if(a[0]+a[-1]<=3.0):
        try:
            del a[0]
            del a[-1]
            c+=1
        except:
            c+=1
    else:
        del a[-1]
        c+=1
print(c)


#input
#5
#1.01 1.99 2.5 1.5 1.01