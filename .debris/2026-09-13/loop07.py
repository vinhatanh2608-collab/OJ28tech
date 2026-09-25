import math 
n = int(input()) 
sl = 0
sum = 0
for i in range(1,math.isqrt(n)+1):
    if n % i == 0:
        sl += 1
        sum += i 
        if n // i != i:
            sl += 1
            sum += n // i
print(sl)
print(sum)