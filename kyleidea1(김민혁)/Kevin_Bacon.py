import sys
input = sys.stdin.readline

n,e = map(int,input().split())
graph = [[987654321]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(e):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

kb_list = [sum([element for element in row if element != 987654321]) for row in graph]

min = 987654321
min_index = n
for i in range(1,n+1):
    if kb_list[i] < min:
        min = kb_list[i]
        min_index = i
print(min_index)