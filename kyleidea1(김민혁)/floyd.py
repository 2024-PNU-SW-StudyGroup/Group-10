import sys
input = sys.stdin.readline
INF = 1e9

n = int(input())
m = int(input())

matrix = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    if c < matrix[a][b]:
        matrix[a][b] = c

for i in range(1,n+1):
    matrix[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])

matrix = [[0 if matrix[j][i] == INF else matrix[j][i] for i in range(1,n+1)] for j in range(1,n+1)]
for row in matrix:
    print(*row)
