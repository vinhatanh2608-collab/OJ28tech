n =int(input())
sum =0
for i in range(1,2*n):
    if i % 2 == 0:
        sum += 1.0/i
print(f"{sum:.5f}")