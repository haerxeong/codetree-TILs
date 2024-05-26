n = int(input())
for i in range(1, 2 * n + 1 + 1):
    if i % 2 == 1:
        print("* " * (2*n + 1))
    else: 
        print("*   " * (n + 1))