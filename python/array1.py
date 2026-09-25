n = int(input())
N = list(map(int ,input().split()))
sochan = 0
sole = 0
tongchan = 0
tongle =0
for i in N:
    if i % 2 ==0:
        sochan +=1
        tongchan +=i
    else:
        sole += 1
        tongle +=i
print(sochan,sole,tongchan,tongle,sep ="\n")