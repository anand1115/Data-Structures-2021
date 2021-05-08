def count(n):
    c=0
    while n:
        n=n&(n-1)
        c+=1
    return c
def check_flips(x,y):
    return count(x^y)
print(check_flips(1,15))
