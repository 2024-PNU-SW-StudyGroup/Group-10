import sys
input = sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
    inp = (input().split())
    
    if inp[0] == 'push':
        stack.append(inp[1])
    elif inp[0] == 'top':
        if not stack:
            print('-1')
        else:
            print(stack[-1])
    elif inp[0] == 'size':
        print(len(stack))
    elif inp[0] == 'pop':
        if stack:
            num = stack.pop()
            print(num)
        else:
            print('-1')
    elif inp[0] == 'empty':
        if not stack:
            print('1')
        else:
            print('0')