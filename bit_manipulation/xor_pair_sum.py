def xor_pair(input_list):
    result=(input_list[0]*2)
    for i in input_list[1:]:
        result^=(i*2)
    return result


print(xor_pair([2,4,1]))