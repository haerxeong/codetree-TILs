n = int(input())
for i in range(1, n + 1):
    print(" "*(n - i), end = '')
    print('* '*i, end = '')
    print()
for j in range(i - 1, 0, -1):
    print(" "*(n - j), end = '')
    print('* '*j, end = '')
    print()