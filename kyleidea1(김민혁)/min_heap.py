import sys
import heapq

input = sys.stdin.readline
n = int(input().strip())
q = []
z = 0
for _ in range(n):
    inp = int(input().strip())
    print(0 if not q else -heapq.heappop(q)) if inp == 0 else heapq.heappush(q,-inp)