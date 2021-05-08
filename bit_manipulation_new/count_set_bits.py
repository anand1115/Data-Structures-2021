def count(num):
    c=0
    while num:
        if(num&1):
            c+=1
        num=num>>1
    return c
print("{:b} count of 1 is {}".format(15,count(15)))
