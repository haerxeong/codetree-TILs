cnt = 1
ans = []
f = 1

n = int(input())
x = int(input())
f = f // abs(f)

for _ in range(1, n):
    x = int(input())
    if f*x > 0: cnt += 1
    else: 
        f *= -1
        ans.append(cnt)
        cnt = 1

print(max(ans))