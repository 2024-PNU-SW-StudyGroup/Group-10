import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def process():
    n, index = map(int, input().split())
    q = deque(list((map(int, input().split()))))
    cnt = 0

    while q:
        v = q.popleft()
        if not q:
            return n
        else:
            if v < max(q):
                q.append(v)
                if index == 0:
                    index = len(q) - 1
                else:
                    index -= 1
            else:
                cnt += 1
                if index == 0:
                    return cnt
                else:
                    index -= 1

for _ in range(T):
    print(process())
