n = int(input())
l = []
for _ in range(n):
    l.append(input())

def is_palindrome(s):
    left = 0
    right = len(s) - 1
    c = 2
    
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if c == 2:
                if s[left+1] == s[right]:
                    left += 1
                    c -= 1
                elif s[left] == s[right-1]:
                    right -= 1
                    c -= 1
                else:
                    return 2
            else:
                return 2
    
    if c == 2:
        return 0
    else:
        return 1

for i in l:
    print(is_palindrome(i))