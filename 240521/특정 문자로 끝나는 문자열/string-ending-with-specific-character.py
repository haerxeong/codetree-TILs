string = []
for _ in range(10): string.append(input())
c = input()
for s in string:
    if s[-1] == c: print(s)