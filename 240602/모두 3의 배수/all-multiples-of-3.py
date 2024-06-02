flag = True
for i in range(5):
    if int(input()) % 3 != 0:
        flag = False
print(int(flag))