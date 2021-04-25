a=int(input())
b=int(input())
c=int(input())
c=0
for i in range(32):
    x=False
    y=False
    z=False
    if(a & 1<<i):
        x=True
    if(b & 1<<i):
        y=True
    if(c & 1<<i):
        z=True
    if(z):
        if(x==False and y==False):
            c+=1
    else:
        if(x and y):
            c+=2
        elif(x or y):
            c+=1
print(c)