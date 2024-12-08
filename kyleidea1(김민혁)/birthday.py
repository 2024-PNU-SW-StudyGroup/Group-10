import sys
input = sys.stdin.readline

n = int(input())
dic = dict()
for _ in range(n):
    parts = input().strip().split()
    dic[parts[0]] = tuple(map(int,parts[1:]))

dic = sorted(dict(sorted(dict(sorted(dic.items(), key = lambda x:x[1][0])).items(), key = lambda x:x[1][1])).items(), key = lambda x:x[1][2])
print(dic[-1][0])
print(dic[0][0])