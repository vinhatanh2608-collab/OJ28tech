import math 
def perfect_square(n):
    N = math.sqrt(n)
    if n <=0 :
        return "ko phải số chính phương"
    else:
        if N * N == n:
            return "số chính phương"
        else:
            return "ko phải số chính phương"
if __name__ == '__main__':
    n =int(input())
    print(perfect_square(n))