# import sys
# from collections import deque
# from collections import deque

# input = sys.stdin.readline

# T = int(input().strip())

# def bfs(k):
#     q = deque()
#     q.append((1, 1))
#     visited = set([(1,1)])
#     cnt = 1

#     while q:
#         cnt += 1
#         for _ in range(len(q)):
#             v = q.popleft()
#             for i in range(-1, 2):
#                 move = v[1] + i
#                 next = (v[0] + move, move)
#                 if move > 0 and next not in visited:
#                     if next[0] == k and move == 1:
#                         return cnt
#                     elif next[0] < k:
#                         q.append(next)
#                         visited.add(next)

# for _ in range(T):
#     s, e = map(int, input().split())
#     print(bfs(e-s))

import sys
import math
from collections import deque
from collections import deque

input = sys.stdin.readline

def get_limit(move):
    n = math.ceil(move/2)
    return n**2 + n if move % 2 == 0 else n**2

def solve(s,e):
    k = e-s
    move, limit = 1, 1
    while k > limit:
        move += 1
        limit = get_limit(move)
    return move

T = int(input())
for _ in range(T):
    s,e = map(int, input().strip().split())
    print(solve(s,e))