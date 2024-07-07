def re(n):
    if n == 1:
        return 1
    return n + re(n - 1)

N = int(input())
print(re(N))