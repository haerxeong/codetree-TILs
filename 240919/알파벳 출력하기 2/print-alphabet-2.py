N = int(input())
char = 0
for i in range(N):
    for j in range(i):
        print(" ", end = " ")
    for k in range(N, i, -1):
        print(chr(char + 65), end = " ")
        char = (char + 1) % 26
    print()