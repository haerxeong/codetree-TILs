n, t = map(int, input().split())
arr = list(map(int, input().split()))
cnt, ans = 0, 0

for i in arr:
    if i > t: cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0

print(max(cnt, ans))