string = list(input())
while len(string) != 1:
    n = int(input())
    if n < len(string): string.pop(n)
    else: string.pop()
    print(''.join(string))