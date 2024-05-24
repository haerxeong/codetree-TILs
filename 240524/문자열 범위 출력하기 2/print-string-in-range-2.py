string = input()
n = int(input())
l = len(string)
print(string[:l-n-1:-1] if n < l else string[::-1])