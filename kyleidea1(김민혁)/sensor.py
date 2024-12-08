import sys
input = sys.stdin.readline

s = int(input())
j = int(input())
l = sorted(list(map(int,input().strip().split())))

if s < j:
    print(0)
else:
    diff = [l[i+1]-l[i] for i in range(s-1)]
    diff.sort()
    for _ in range(j-1):
        diff.pop()

    print(sum([i for i in diff]))