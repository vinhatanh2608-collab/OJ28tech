import math 
def prime(x):
    if x < 2 :
        return 0
    for i in range(2,math.isqrt(x)+1):
        if x % i == 0:
            return 0
    return 1

n = int(input())
N = list(map(int ,input().split()))
tong = 0
dem = 0
for i in N:
    if prime(i):
        tong += i
        dem += 1
ketqua = tong / dem
print(f"{ketqua:.3f}")