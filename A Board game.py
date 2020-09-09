import numpy as np
import array as ar
N = int(input())
r =N;c=N
arr1 = np.arange(N*N).reshape(r,c)
for i in range(r):
    li = [int(x) for x in input().split()]
    for j in range(c):
        arr1[i][j] = li[j]
i = 0
j = 0
score = 0
while(i<r-1 and j<=r-1):
    if(j<c-1):
        if(arr1[i+1][j] > arr1[i][j+1]):
            j += 1
            score = score//2 + arr1[i][j]
            
        elif(arr1[i][j+1] > arr1[i+1][j]):
            i += 1
            score = score//2 + arr1[i][j]
    else:
        i += 1
        score = score//2 + arr1[i][j]
print(score)
