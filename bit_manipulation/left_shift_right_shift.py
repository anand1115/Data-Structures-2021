def left_shift_anybase(num,base,left):
    return num*(base**left)

def right_shift_anybase(num,base,right):
    return num//(base**right)
print(left_shift_anybase(10,2,2),10<<2)
print(right_shift_anybase(10,2,2),10>>2)
