import sys
import heapq

input = sys.stdin.readline

l = [[] for _ in range(100001)]
n = int(input())

for _ in range(n):
    num,dif = map(int,input().split())
    l[dif].append(num)

m = int(input())
for _ in range(m):
    cmd = input().split()
    if cmd[0] == 'recommend':
        if cmd[1] == '1':
            
    
