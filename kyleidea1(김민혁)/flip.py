num = input()
zero = 0
one = 0

for i in range(1, len(num)):
    if num[i-1] == '0' and num[i] == '1':
        zero += 1
    if num[i-1] == '1' and num[i] == '0':
        one += 1

if num[-1] == '0':
    zero += 1
else:
    one += 1

print(min(zero, one))
