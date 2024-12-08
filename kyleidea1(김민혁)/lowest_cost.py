import sys
import heapq

input = sys.stdin.readline
INF = 100001
n = int(input())
e = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

distance = [INF] * (n+1)
s,e = map(int, input().split())

def dijkstra(start, end):
    q = []
    distance[start] = 0
    heapq.heappush(q, (start, 0))
    
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for e, d in graph[now]:
            cost = dist + d
            if cost < distance[e]:
                distance[e] = cost
                heapq.heappush(q, (e, cost))
    return distance[end]

print(dijkstra(s,e))