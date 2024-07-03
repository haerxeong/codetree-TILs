from itertools import combinations as cb

n = int(input())
li = list(map(int, input().split()))

cnt = 0
arr = [i for i in range(n)]

for i, j, k in cb(arr, 3):
    if li[i] <= li[j] <= li[k]:
        cnt += 1
print(cnt)