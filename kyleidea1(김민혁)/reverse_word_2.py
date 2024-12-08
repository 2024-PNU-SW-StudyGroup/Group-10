import sys
input = sys.stdin.readline

inp = input().strip()
tag = False
ans = ''
tmp = ''

for i in range(len(inp)):
    if not tag:
        if inp[i] == '<':
            tag = True
            ans += tmp[::-1]
            ans += '<'
            tmp = ''
        else:
            if inp[i] == ' ':
                ans += tmp[::-1]
                ans += ' '
                tmp = ''
            else:
                tmp += inp[i]
    else:
        if inp[i] == '>':
            ans += '>'
            tag = False
        else:
            ans += inp[i]
ans += tmp[::-1]
    
print(ans)