import sys

n = int(input())

graph = []
res = []
size = 0

for _ in range(n):
    tmp = input()
    l = [int(i) for i in tmp]
    graph.append(l)

def dfs(x, y):
    global size
    if x < 0 or y < 0 or x >= n or y >= n or graph[x][y] == 0:
        return False
    graph[x][y] = 0
    size += 1
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True

cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            if dfs(i,j):
                cnt += 1
            res.append(size)
            size = 0
res.sort()

print(cnt)
for i in range(len(res)):
    print(res[i])
