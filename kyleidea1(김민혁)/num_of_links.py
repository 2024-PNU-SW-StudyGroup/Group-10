# from collections import deque

# n, e = map(int, input().split())
# l = [[] for _ in range(n+1)]
# for _ in range(e):
#     a, b = map(int, input().split())
#     l[a].append(b)
#     l[b].append(a)
# visited = [False] * (n+1)
# visited[0] = True

# cnt = 0
# for i in range(1,n+1):
#     if not visited[i]:
#         q = deque([i])
#         visited[i] = True
#         cnt += 1
#         while q:
#             v = q.popleft()
#             for child in l[v]:
#                 if not visited[child]:
#                     visited[child] = True
#                     q.append(child)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n+1)
cnt = 0

def dfs(graph, v, visited):
    global cnt
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
for i in range(1,n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1

print(cnt)



