def dec_to_any_base(num,base):
    final=""
    while num>0:
        rem=num%base
        if(rem<10):
            final+=str(rem)
        else:
            final+=chr(55+rem)
        num=num//base
    return final[::-1]

def any_base_to_dec(num,base):
    num=str(num)
    num=num[::-1]
    final=0
    for i in range(len(num)):
        dig=num[i]
        if(dig.isnumeric()):
            dig=int(dig)
        else:
            dig=ord(dig.upper())-55
        final+=dig*(base**i)    
    return final    

print(dec_to_any_base(8,2))
print(dec_to_any_base(15,16))
print(dec_to_any_base(8,8))
print(any_base_to_dec(1000,2))
print(any_base_to_dec('F',2))
print(any_base_to_dec(8,8))