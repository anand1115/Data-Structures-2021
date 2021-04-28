def getMinTrips(weights):
    weights.sort()
 
    trips = 0
    left_index = 0
    for i in range(n-1, -1, -1):
        if(weights[i] > 1.99):
            trips+=1
        if(weights[i]<=1.99):
            if(weights[i]+weights[left_index]<=3):
                left_index+=1
            trips+=1
        if(left_index>=i):
            break
 
    return trips
 
 
n = int(input())
weights = list(map(float, input().split()))
trips = getMinTrips(weights)
print(trips)

#input
#5
#1.01 1.99 2.5 1.5 1.01