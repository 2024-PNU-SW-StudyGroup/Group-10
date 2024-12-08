import sys
import heapq

input = sys.stdin.readline
n, m, x = map(int, input().split())
INF = 1e9

graph = [[] for _ in range(n+1)]
dist_from_X = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

dist_to_X = [0] * (n+1)
for i in range(1, n+1):
    distance = [INF] * (n+1)
    if i == x:
        dist_from_X = dijkstra(i, distance)
    else:
        dist_to_X[i] = dijkstra(i, distance)[x]

ans = max([dist_to_X[i] + dist_from_X[i] for i in range(1,n+1)])
print(ans)