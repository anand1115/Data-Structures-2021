"""
Problem Statement:---
You want to reach heaven that is at the top of this staircase.the staircase has n steps.
and at each step you can climb either 1 or 2 steps further.how many ways can you reach heaven?

"""
steps=int(input())
ways=[0]*(steps+1)
ways[0]=1
ways[1]=2
for i in range(2,steps+1):
    ways[i]=ways[i-1]+ways[i-2]
print(ways)
print(ways[steps])