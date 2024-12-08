num = input()

if '0' not in num:
    print(-1)
else:
    sum = 0
    num.replace('0','',1)
    for n in num:
        sum += int(n)
    if sum % 3 == 0:
        ans = sorted(num, reverse=True)
        print(''.join(ans))
    else:
        print(-1)
