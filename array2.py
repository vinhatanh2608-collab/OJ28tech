import math
def prime(n):
    if n < 2:
        return 0
    for i in range(2,math.isqrt(n)+1):
        if n % i == 0:
            return 0
    return 1
n = int(input())
A = list(map(int ,input().split()))
tong = 0
dem = 0
for i in A:
    if prime(i):
        tong += i
        dem += 1
ket_qua = tong / dem
print(f"{ket_qua:.3f}")