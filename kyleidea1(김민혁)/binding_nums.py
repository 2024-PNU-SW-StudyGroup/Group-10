import sys
import heapq
input = sys.stdin.readline

n = int(input())
pos_q = []
neg_q = []
for _ in range(n):
    num = int(input())
    if num > 0:
        heapq.heappush(pos_q,-num)
    else:
        heapq.heappush(neg_q,num)

sum = 0
while pos_q:
    for _ in range(len(pos_q)//2):
        a = -heapq.heappop(pos_q)
        b = -heapq.heappop(pos_q)
        sum += (a*b) if a*b > a+b else (a+b)
    if pos_q:
        sum += (-heapq.heappop(pos_q))

while neg_q:
    for _ in range(len(neg_q)//2):
        a = heapq.heappop(neg_q)
        b = heapq.heappop(neg_q)
        sum += (a*b)
    if neg_q:
        sum += heapq.heappop(neg_q)

print(sum)
    
