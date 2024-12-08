import sys
input = sys.stdin.readline
from collections import deque

start = list(map(str,input().strip()))
target = list(map(str,input().strip()))


def solve(start, target):
    while target:
        if target[-1] == 'B':
            target.pop()
            target = target[::-1]
        elif target[-1] == 'A':
            target.pop()
        if target == start:
            return 1
    return 0

print(solve(start,target))