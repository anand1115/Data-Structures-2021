price=[8,1,2,4,6,3]
n=len(price)
min_uptil=[0]*n
profit=[0]*n
min_uptil[0]=price[0]
for i in range(1,n):
    min_uptil[i]=min(min_uptil[i-1],price[i])
for i in range(n):
    profit[i]=price[i]-min_uptil[i]
print(max(profit))