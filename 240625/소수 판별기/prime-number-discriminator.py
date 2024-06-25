n = int(input())
flag = True
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        flag = False
print("P" if flag else "C")