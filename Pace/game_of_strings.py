a=input().lower()
b=input().lower()
k=int(input())
if(len(a)==len(b)):
    for i in range(len(a)):
        diff=abs(ord(b[i])-ord(a[i]))   
        if(diff<=k):
            continue
        else:
            print("No")
            break
    else:
        print("YES")

