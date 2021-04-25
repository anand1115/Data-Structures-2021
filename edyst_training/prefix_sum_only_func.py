def prefix_sum(k):
    sum_list=[None]*len(k)
    for i in range(len(k)):
        if(i==0):
            sum_list[i]=k[i]
        else:
            sum_list[i]=sum_list[i-1]+k[i]
    return sum_list
input_list=list(map(int,input().split()))
print(prefix_sum(input_list))