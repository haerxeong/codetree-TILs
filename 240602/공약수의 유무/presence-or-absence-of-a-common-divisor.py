flag = False
a, b = map(int, input().split())
for i in range(a, b + 1):
    if 1920 % i == 0 and 2880 % i == 0:
        flag = True
        break
print(int(flag))