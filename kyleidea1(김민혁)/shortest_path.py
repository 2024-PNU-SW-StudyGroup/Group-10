import sys
import heapq

input = sys.stdin.readline
INF = 987654321

v, e = map(int, input().split())
s = int(input())

graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue
        for i in graph[cur]: # graph[cur]은 현재 노드에서 갈 수 있는 놈들
            cost = dist + i[1] # 현재 보고 있는 놈을 통해서 다음 노드로 가는 비용
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
        
dijkstra(s)

for i in range(1,v+1):
    print(distance[i] if distance[i] != INF else 'INF')
