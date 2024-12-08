import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def solve(p, l):
    R_is_odd = False
    for x in p:
        if x == 'R':
            R_is_odd = not R_is_odd
        elif x == 'D':
            if not l:
                return 'error'
            else:
                l.pop() if R_is_odd else l.popleft()
    result = list(l)[::-1] if R_is_odd else list(l)
    return "[" + ",".join(map(str, result)) + "]"

for _ in range(T):
    p = input().strip()
    n = int(input())
    arr_str = input().strip()
    if n == 0:
        l = deque([])
    else:
        l = deque(map(int, arr_str[1:-1].split(',')))
    print(solve(p, l))
