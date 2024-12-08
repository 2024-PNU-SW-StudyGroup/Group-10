import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]

ps = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            ps[i][j] = l[i][j]
        elif i == 0:
            ps[i][j] = ps[i][j-1] + l[i][j]
        elif j == 0:
            ps[i][j] = ps[i-1][j] + l[i][j]
        else:
            ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + l[i][j]

for _ in range(m):
    y1, x1, y2, x2 = map(int, input().split())
    y1, x1, y2, x2 = y1 - 1, x1 - 1, y2 - 1, x2 - 1
    
    result = ps[y2][x2]
    if y1 > 0:
        result -= ps[y1-1][x2]
    if x1 > 0:
        result -= ps[y2][x1-1]
    if y1 > 0 and x1 > 0:
        result += ps[y1-1][x1-1]
    
    print(result)