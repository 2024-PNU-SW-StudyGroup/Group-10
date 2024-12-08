import sys
import heapq

input = sys.stdin.readline

def solution():
    n = int(input())
    crane = list(map(int,input().split()))
    m = int(input())
    box = list(map(int,input().split()))

    if max(box) > max(crane):
        return -1
    
    crane_heap = []
    for c in crane:
        heapq.heappush(crane_heap, -c)
    box_heap = []
    for b in box:
        heapq.heappush(box_heap, -b)

    cnt = 0
    while box_heap:
        cnt += 1
        for _ in range(n):
            if not box_heap:
                break
            if -box_heap[0] <= -crane_heap[0]:
                heapq.heappop(box_heap)
            heapq.heappop(crane_heap)
            if crane_heap:
                heapq.heappush(crane_heap, -crane_heap[0])
    return cnt

print(solution())