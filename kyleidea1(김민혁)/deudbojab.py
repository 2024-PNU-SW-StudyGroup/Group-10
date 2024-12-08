import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

dictionary = dict()
for i in range(n):
    word = input().rstrip()
    dictionary[word] = True

ans = []
for j in range(m):
    key = input().rstrip()
    if key in dictionary:
        ans.append(key)
ans.sort()

print(len(ans))
for a in ans:
    print(a)
