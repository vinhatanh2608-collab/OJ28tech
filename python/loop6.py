import math
n =int(input())
sum = 0
for i in range(1,math.isqrt(n)+1):
    if n % i ==0:
        sum += i
        if n // i != i: #16 // 4 ==4 không cộng vào
            sum += n//i
print(sum)