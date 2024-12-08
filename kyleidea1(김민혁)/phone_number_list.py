import sys
input = sys.stdin.readline

def solve():
    n = int(input())

    l = []
    for _ in range(n):
        l.append(input().strip())
    l.sort()
    
    for i in range(len(l)-1):
            if l[i+1].startswith(l[i]):
                return 'NO'
            
    return 'YES'

T = int(input())
for _ in range(T):
    print(solve())