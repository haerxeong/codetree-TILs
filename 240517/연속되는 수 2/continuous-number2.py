arr = []
cnt = 1
max_cnt = 0
n = int(input())
for _ in range(n):
    arr.append(int(input()))

for i in range(1, n):
    if arr[i] == arr[i - 1]:
        cnt += 1
    else:
        if max_cnt < cnt:
            max_cnt = cnt
        cnt = 1

if max_cnt < cnt:
    max_cnt = cnt

print(max_cnt)