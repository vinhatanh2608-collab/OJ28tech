n = int(input())
A = list(map(int ,input().split()))
sochan = 0
sole = 0
sumchan = 0 
sumle =0
for i in A:
    if i % 2 == 0:
        sochan += 1
        sumchan += i
    else:
        sole += 1
        sumle += i
print(sochan,sole,sumchan,sumle,sep="\n")