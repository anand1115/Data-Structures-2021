def round(num):
    if(num&(num-1)==0):
        return num
    else:
        while num&(num-1):
            num=num&(num-1)
        return num<<1
def round_min(n):
    if(n&(n-1)==0):
        return n
    else:
        while n&(n-1):
            n=n&(n-1)
        return n
print(round(16))
print(round_min(15))

