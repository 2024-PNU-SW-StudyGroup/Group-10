import sys
input = sys.stdin.readline

n = int(input())
words = []
for _ in range(n):
    words.append(input().strip())

def voca_checker(word):
    alps = 'abcdefghijklmnopqrstuvwxyz'
    dictionary = dict(zip(list(alps),[False]*len(alps)))
    cur = word[0]
    dictionary[cur] = True
    for i in range(1, len(word)):
        cur = word[i]
        if word[i] != word[i-1]:
            if dictionary[cur]:
                return False
            else:
                dictionary[cur] = True
    return True

print([voca_checker(words[i]) for i in range(n)].count(True))