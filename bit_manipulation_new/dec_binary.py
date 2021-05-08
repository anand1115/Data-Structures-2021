def convert(num,base):
    final=""
    while num:
        rem=num%base
        if(rem<10):
            final+=str(rem)
        else:
            final+=chr(rem+55)
        num//=base
    return final[::-1]
def convert_dec(num,base):
    num=str(num)[::-1]
    final=0
    for i in range(len(num)):
        dig=num[i]
        if(dig.isnumeric()):
            dig=int(dig)
        else:
            dig=ord(dig.upper())-55
        final+=(dig*(base**i))
    return final
print(convert_dec('1111',2))
            
