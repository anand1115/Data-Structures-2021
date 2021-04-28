def is_perfect(N):
    if N == 1:
        return False
 
    i = 2
    divisors = set([1])
 
    while i * i <= N:
        if N % i == 0:
            divisors.add(i)
            divisors.add(N // i)
 
        i += 1
 
    return sum(divisors) == N
 
 
T = int(input())
 
for i in range(T):
    N = int(input())
    if is_perfect(N):
        print("YES")
    else:
        print("NO")
 