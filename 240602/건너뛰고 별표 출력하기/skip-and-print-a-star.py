n = int(input())
for i in range(n):
    print('*' * (i + 1))
    print()
for j in range(i, 0, -1):
    print('*' * j)
    print()