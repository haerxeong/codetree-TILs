n = int(input())
for i in range(n):
    if i % 2 == 0:
        cnt = 1
        for j in range(n):
            print(cnt, end = '')
            cnt += 1
    else:
        cnt = n
        for j in range(n):
            print(cnt, end = '')
            cnt -= 1
    print()