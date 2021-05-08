def find_right_most_set(num):
    k=num^(num & (num-1))
    k="{:b}".format(k)
    k=k[::-1]
    return k.find("1")+1
from math import log
def alternate(num):
    return log(num & (-num),2)+1
print(find_right_most_set(20))
print(int(alternate(1)) )

