def divide(a,b):
    while(a%b==0):
        a=a/b
    return a

def isugly(number):
    number=divide(number,2)
    number=divide(number,3)
    number=divide(number,5)
    return 1 if number==1 else 0

n=int(input())

count=1
ugly=[1]
i=2
while count<n:
    if(isugly(i)):
        count+=1
        ugly.append(i)
    i+=1
print(ugly)
print(ugly[n-1])


