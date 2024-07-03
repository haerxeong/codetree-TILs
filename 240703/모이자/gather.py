n = int(input())
li = list(map(int, input().split()))
ans = [0]*n
for i in range(1, n + 1): #모이는 장소
    for j in range(1, n + 1): #각 집의 이동 거리
        if i==j: continue
        ans[i-1] += li[j-1] * abs(i - j)

print(min(ans))