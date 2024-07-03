from itertools import combinations as cb
cnt = 0
A = input()
for s in cb(A, 2):
    if s == ('(', ')'):
        cnt += 1
print(cnt)