import sys

a = 0
b = 0
c = 0
s = input()
prev = 0
prev2 = 0
answer = ''

for char in s:
    if char == 'A':
        a += 1
    elif char == 'B':
        b += 1
    else:
        c += 1

for i in range(len(s)):
    if b - 1 == a + c and prev != 1 and b > 0:
        answer += 'B'
        prev2 = prev
        prev = 1
        b -= 1
    elif 2 * (c - 1) == a + b and prev != 2 and prev2 != 2 and c > 0:
        answer += 'C'
        prev2 = prev
        prev = 2
        c -= 1
    else:
        if c > 0 and prev != 2 and prev2 != 2:
            answer += 'C'
            prev2 = prev
            prev = 2
            c -= 1
        elif b > 0 and prev != 1:
            answer += 'B'
            prev2 = prev
            prev = 1
            b -= 1
        elif a > 0:
            answer += 'A'
            prev2 = prev
            prev = 0
            a -= 1
        else:
            print(-1)
            sys.exit()

print(answer)
