import math
n=int(input())
for i in range(n):
    k=int(input())
    if(k&1==1):
        print("NO")
    else:
        sum=1
        for j in range(2,int(math.sqrt(k))+1):
            if(k%j==0):
                sum+=j+(k//j)
        if(sum==k):
            print("YES")
        else:
            print("NO")
            
            
#3
#6
#5
#28