A = input()
prev = A[0]
ans = A[0]
cnt = 1
for s in A[1::]:
    if s == prev:
        cnt += 1
    else:
        ans += str(cnt)
        ans += s
        cnt = 1
        prev = s
ans += str(cnt)
print(len(ans))
print(ans)