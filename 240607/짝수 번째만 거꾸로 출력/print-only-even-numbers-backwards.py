s = input()
ans = ''
for i in range(1, len(s) + 1, 2):
    ans += s[i]
print(''.join(ans[::-1]))