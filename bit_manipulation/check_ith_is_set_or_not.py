def check(num,i):
    return num==(num and (1<<i))
k=int(input("Enter Number : "))
i=int(input("enter digit place : "))
print(check(k,i))