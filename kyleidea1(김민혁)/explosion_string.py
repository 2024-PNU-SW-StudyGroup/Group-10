import sys
input = sys.stdin.readline

s = input().rstrip()
bomb = input().rstrip()

stack = []

for l in s:
    stack.append(l)
    if len(stack) >= len(bomb):
        if stack[-len(bomb):] == list(bomb):
            for _ in range(len(bomb)):
                stack.pop()

print(''.join(stack) if stack else 'FRULA')