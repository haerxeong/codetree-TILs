plane = [[0]*201 for _ in range(201)]
offset = 100
c = ['r', 'b']
index = 0

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += offset; y1 += offset; x2 += offset; y2 += offset
    for i in range(x1, x2):
        for j in range(y1, y2):
            plane[i][j] = c[index]

    index = (index + 1)%2

print(sum(row.count('b') for row in plane))