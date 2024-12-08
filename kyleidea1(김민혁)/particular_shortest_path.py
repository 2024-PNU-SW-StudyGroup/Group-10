import sys
import heapq
input = sys.stdin.readline
INF = 1e9

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
original_distance = [INF] * (n+1)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
p1, p2 = map(int, input().split())

def dijkstra(start,end):
    q = []
    heapq.heappush(q, (start, 0))

    distance = original_distance[:]
    distance[start] = 0

    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for e,d in graph[now]:
            cost = dist + d
            if cost < distance[e]:
                distance[e] = cost
                heapq.heappush(q, (e, cost))
    return distance[end]

path_1 = dijkstra(1,p1) + dijkstra(p1,p2) + dijkstra(p2,n)
path_2 = dijkstra(1,p2) + dijkstra(p2,p1) + dijkstra(p1,n)
print(-1 if path_1 >= INF and path_2 >= INF else min(path_1,path_2))
