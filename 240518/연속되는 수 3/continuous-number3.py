cnt = 1
ans = []

n = int(input())
x = int(input())
f = x // abs(x)

for _ in range(1, n):
    x = int(input())
    if f*x > 0: cnt += 1
    else: 
        f *= -1
        ans.append(cnt)
        cnt = 1

ans.append(cnt)

print(max(ans))