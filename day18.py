import math

def countDivisors(N: int) -> int:
    count = 0
    for i in range(1, int(math.isqrt(N)) + 1):
        if N % i == 0:  
            if i == N // i: 
                count += 1
            else:
                count += 2
    return count
