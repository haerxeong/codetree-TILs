n = int(input())
ans = ''
ans += input().replace(" ", "")
while ans != '':
    print(ans[:5])
    ans = ans[5::]