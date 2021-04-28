m=int(input("Enter the row value : "))
n=int(input("Enter the column Value : "))
ways=[[0]*n for i in range(m)]
for i in range(n-1):
    ways[m-1][i]=1
for j in range(m-1):
    ways[j][n-1]=1

for i in range(m-2,-1,-1):
    for j in range(n-2,-1,-1):
        ways[i][j]=ways[i][j+1]+ways[i+1][j]

print(ways[0][0])