def turn_on(num,k):
    return num|((1<<k-1))
def turn_off(num,k):
    return num&(~(1<<k-1))
def check_on(num,k):
    return True if(num&(1<<k-1)) else False
k=15
print("{:b} before off,after off {:b}".format(k,turn_off(k,2)))
print("{:b} before off,after off {:b}".format(k,turn_on(k,2)))
print("{:b} check on at 3,{}".format(k,check_on(k,3)))
