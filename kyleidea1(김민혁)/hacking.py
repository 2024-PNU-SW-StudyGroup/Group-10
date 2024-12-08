import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, e, s = map(int, input().split())
    INF = 1e9

    graph = [[] for _ in range(n+1)]

    for _ in range(e):
        a, b, d = map(int, input().split())
        graph[b].append((a,d))

    distance = [INF] * (n+1)
    distance[s] = 0

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for child in graph[now]:
                cost = dist + child[1]
                if cost < distance[child[0]]:
                    distance[child[0]] = cost
                    heapq.heappush(q, (cost, child[0]))

    dijkstra(s)

    l = [i for i in distance if i != INF]
    print(len(l), end = ' ')
    print(max(l))
