def AtoDec(A, N):
    ans = 0
    for i in range(len(N)):
        ans += int(N[-1-i]) * A**i
    return ans

def DectoB(dec, B):
    ans = ''
    while dec:
        ans += str(dec % B)
        dec //= B
    return ans[::-1]

A, N, B = input().split()
A, B = int(A), int(B)

print(DectoB(AtoDec(A, N), B))