import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
card = list(map(int, input().split()))
pq = []
for c in card:
    heapq.heappush(pq, c)

for _ in range(k):
    c1 = heapq.heappop(pq)
    c2 = heapq.heappop(pq)
    heapq.heappush(pq, c1+c2)
    heapq.heappush(pq, c1+c2)

print(sum(pq))
