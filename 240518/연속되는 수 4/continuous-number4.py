n = int(input())
arr = [int(input()) for _ in range(n)]

ans, cnt = 0, 1
for i in range(1, n):
    if arr[i] > arr[i - 1]:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1

print(max(ans, cnt))