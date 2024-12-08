import sys
from collections import deque

input = sys.stdin.readline

f,s,g,u,d = map(int,input().split())

def bfs():
    visited =[False]*(f+1)
    q = deque()
    q.append((s,0))
    visited[s] = True

    while q:
        cur,cnt = q.popleft()
        if cur == g:
            return cnt
        else:
            up,down = cur+u,cur-d
            if 1<=up<=f and not visited[up]:
                q.append((up,cnt+1))
                visited[up] = True
            if 1<=down<=f and not visited[down]:
                q.append((down,cnt+1))
                visited[down] = True
    return -1

ans = bfs()
print(ans if ans != -1 else 'use the stairs')