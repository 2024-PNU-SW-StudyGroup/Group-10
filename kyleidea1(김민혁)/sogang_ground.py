import sys
import heapq
input = sys.stdin.readline
INF = 1e9

n,m,r = map(int,input().split())
items = [0] + list(map(int,input().split()))
graph = [[] for _ in range(n+1)]


for _ in range(r):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


def dijkstra(start):
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue
        for next,cost in graph[cur]:
            via = distance[cur] + cost
            if via < distance[next]:
                distance[next] = via
                heapq.heappush(q,(via,next))
    return sum(items[i] for i in range(1,n+1) if distance[i] <= m)

num_items = []
for i in range(1,n+1):
    num_items.append(dijkstra(i))
print(max(num_items))