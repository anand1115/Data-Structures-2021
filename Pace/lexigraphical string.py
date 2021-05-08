from itertools import permutations
n=int(input())
for i in range(n):
    s=input()
    k=sorted(list(permutations(s,len(s))))
    for i in k:
        i="".join(i)
        if(i>s):
            print(i)
            break
    else:
        print("No Answer")
