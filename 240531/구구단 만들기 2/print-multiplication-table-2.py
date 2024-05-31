a, b = map(int, input().split())
for i in [2, 4, 6, 8]:
    for j in range(b, a-1, -1):
        print(f"{j} * {i} = {i*j}", end = ' / ' if j != a else '\n')