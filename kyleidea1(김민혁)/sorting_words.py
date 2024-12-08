n = int(input())

words = list(set([input() for _ in range(n)]))
words.sort()
ans = sorted(words, key = lambda x: len(x))
for a in ans:
    print(a)