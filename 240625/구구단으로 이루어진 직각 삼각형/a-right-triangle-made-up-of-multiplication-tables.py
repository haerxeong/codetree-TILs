n = int(input())
for i in range(1, n + 1):
    for j in range(1, n - i + 2):
        if j == n - i + 1: e = '\n'
        else: e = ' / '
        print(f"{i} * {j} = {i*j}", end = e)