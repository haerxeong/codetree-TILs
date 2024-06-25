a, b, c = map(int, input().split())
flag = True
for i in range(a, b + 1):
    if i % c == 0:
        flag = False
print("YES" if flag else "NO")