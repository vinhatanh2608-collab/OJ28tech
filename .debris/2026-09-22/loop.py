import math
def prime1(n):
    for i in range(2,math.isqrt(n)+1):
        if n % i == 0: 
            return 0
        else: 
            return 1
def prime2(n):
    if n < 2 : return 0
    for j in range(2,n+1):
        if n % j != 0:
            print(j ,end =" ")

if __name__ == '__main__':
    n = int(input())
    if prime1(n):
        print("YES")
    else:
        print("NO")