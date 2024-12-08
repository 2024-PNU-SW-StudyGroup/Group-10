import sys

n = int(sys.stdin.readline().strip())
l = []
for _ in range(n):
    w = int(sys.stdin.readline().strip())
    l.append(w)

l = sorted(l, reverse = True)
maximum = l[0]

for i in range(1,len(l)+1):
    if i * l[i-1] > maximum:
        maximum = i * l[i-1]
print(maximum)