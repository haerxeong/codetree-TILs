n = int(input())
k = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        for j in range(k + 1, k + n + 1):
            print(j, end = ' ')
    else:
        for k in range(j + 2, j + (n * 2) + 1, 2):
            print(k, end = ' ')
    print()