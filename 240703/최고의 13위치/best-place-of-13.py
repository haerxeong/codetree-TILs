n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

max_cnt = 0

for i in range(n):
    for j in range(n - 2):
        max_cnt = max(max_cnt, li[i][j] + li[i][j+1] + li[i][j+2])

print(max_cnt)