import sys
input = sys.stdin.readline

def check(s):
    stack = []
    for char in s:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                return 'no'
        elif char == ']':
            if not stack or stack.pop() != '[':
                return 'no'
    return 'yes' if not stack else 'no'

while True:
    s = input().rstrip()
    if s == '.':
        break
    else:
        print(check(s))