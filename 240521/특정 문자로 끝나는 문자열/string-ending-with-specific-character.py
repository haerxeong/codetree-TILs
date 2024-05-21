string = []
for _ in range(10): string.append(input())
c = input()
cnt = 0
for s in string:
    if s[-1] == c: print(s); cnt += 1

if cnt == 0: print("None")