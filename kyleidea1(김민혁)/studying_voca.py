from collections import Counter
import sys

v = sys.stdin.readline().upper().rstrip()

counter = Counter(v)
c = sorted(counter.items(), key = lambda x: x[1], reverse = True)

if len(c) == 1:
    print(c[0][0])
else:
    if c[0][1] != c[1][1]:
        print(c[0][0])
    else:
        print('?')