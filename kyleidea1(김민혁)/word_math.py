from collections import Counter

n = int(input())

l = []
alp_set = {}
for _ in range(n):
    x = list(input())
    l.append(x[::-1])

total = []
for i in l:
    total.extend(i)
alp_set = set(total)

dictionary = dict(zip(alp_set, [0]*len(alp_set)))
print(dictionary)

def set_number(alps, nums):
    counter = sorted(Counter(alps), key = lambda x:x[1], reverse=True)
    for i in range(len(alps)):
        


while True:
    i = 0
    n = 9
    tmp = []
    for word in l:
        tmp.append(word[i])

