import sys
import math
from collections import deque
input = sys.stdin.readline

def check(x,y,cx,cy):
    return abs(cx-x)+abs(cy-y)

def solve():
    n = int(input())
    sx,sy = map(int,input().split())
    con = []
    for _ in range(n):
        x,y = map(int,input().split())
        con.append((x,y))
    dx,dy = map(int,input().split())

    q = deque()
    visited = set([])
    q.append((sx,sy))
    visited.add((sx,sy))

    while q:
        x,y = q.popleft()
        if check(x,y,dx,dy) <= 1000:
            return 'happy'
        for cx,cy in con:
            if check(x,y,cx,cy)<=1000 and (cx,cy) not in visited:
                q.append((cx,cy))
                visited.add((cx,cy))
    return 'sad'

T = int(input())
for _ in range(T):
    print(solve())