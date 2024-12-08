import heapq
import sys

s, e = map(int, input().split())
graph = [[] for _ in range(100001)]
graph[0] = [(1,1)]
distance = [1e9] * 100001

for i in range(1,50001):
    graph[i].append((i+1,1))
    graph[i].append((i-1,1))
    graph[i].append((2*i,0))
for i in range(50001,100001):
    graph[i].append((i+1,1))
    graph[i].append((i-1,1))

q = []
heapq.heappush(q, (s, 0))
distance[s] = 0

while q:
    now, dist = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for dest, d in graph[now]:
        if dest < 0 or dest > 100000:
            continue
        cost = dist + d
        if cost < distance[dest]:
            distance[dest] = cost
            heapq.heappush(q, (dest, cost))
    
print(distance[e])

    
 