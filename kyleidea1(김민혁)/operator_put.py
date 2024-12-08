import sys
from collections import deque

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
ops = list(map(int, sys.stdin.readline().split()))
q = deque([(num[0], ops)])

def operation(i,a,b):
    if i == 0:
        return a + b
    elif i == 1:
        return a - b
    elif i == 2:
        return a * b
    else:
        if a < 0:
            return -((-a) // b)
        else:
            return a // b

for i in range(1,n):
    for j in range(len(q)):
        v, num_ops = q.popleft()
        for j in range(4):
            if num_ops[j] > 0:
                tmp = num_ops[:]
                tmp[j] -= 1
                q.append((operation(j,v,num[i]), tmp))
print(max(pair[0] for pair in q))
print(min(pair[0] for pair in q))

