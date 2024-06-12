a = input()
b = input()

cnt = sum(1 for i in range(len(a)-1) if a[i:i+2] == b)

print(cnt)