import heapq
import sys

n = int(input())
q = []

for _ in range(n):
    s,e = map(int, sys.stdin.readline().strip().split())
    q.append((s,e))
q.sort()

h = []
heapq.heappush(h, q[0][1])

for i in range(1,n):
    if q[i][0] >= h[0]:
        heapq.heappop(h)
        heapq.heappush(h, q[i][1])
    else:
        heapq.heappush(h, q[i][1])

print(len(h))