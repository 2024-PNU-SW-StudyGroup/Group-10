import sys
import heapq
input = sys.stdin.readline
INF = 1e9

n, m = map(int, input().split())
graph = [[(i+1,1)] for i in range(m+1)]
for _ in range(n):
    a,b,c = map(int, input().split())
    if b-a > c and b <= m:
        graph[a].append((b,c))
graph[m] = [(m,0)]
distance = [INF] * (m+1)
distance[0] = 0

q = []
heapq.heappush(q, (0,0))
while q:
    now, dist = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for e,d in graph[now]:
        cost = dist + d
        if cost < distance[e]:
            distance[e] = cost
            heapq.heappush(q, (e, cost))

print(distance[m])