import sys; input = sys.stdin.readline

n,m,inven = map(int,input().split())
matrix = [[] for _ in range(n)]
for i in range(n):
    matrix[i] = (list(map(int,input().split())))
time = 0

while True:
    maxx = max([max(row) for row in matrix])
    minn = min([min(row) for row in matrix])
    for i in range(n):
        for j in range(m):
            
def check_if_flat(matrix):
    element = matrix[0][0]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != element:
                return False
    return True
