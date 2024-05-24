arr = []
cnt, l = 0, 0
for _ in range(int(input())):
    arr.append(input())
c = input()

for s in arr:
    if s[0] == c:
        cnt += 1
        l += len(s)
print(f"{cnt} {l/cnt:.2f}")