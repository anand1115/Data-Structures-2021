def prefix_sum(input_list):
    prefix=[None]*len(input_list)
    for i,v in enumerate(input_list):
        if(i==0):
            prefix[i]=v
        else:
            prefix[i]=prefix[i-1]^v
    return prefix

def queries(input_list,q):
    prefix=prefix_sum(input_list)
    for i in q:
        if(i[0]==0):
            print(prefix[i[1]],end=" ")
        else:
            l=i[0]-1
            r=i[1]
            print(prefix[r]^prefix[l],end=" ")
        
queries([1,3,4,8],[[0,1],[1,2],[0,3],[3,3]])

