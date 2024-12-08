n = int(input())

s = [True]*(n+1)
s[0],s[1] = False, False
prime = []

for i in range(2,n+1):
    if s[i]:
        prime.append(i)
        for j in range(2*i,n+1,i):
            s[j] = False

l = 0
part_sum = 0
cnt = 0

for r in range(len(prime)):
    part_sum += prime[r]
    while part_sum >= n:
        if part_sum == n:
            cnt += 1
        part_sum -= prime[l]
        l += 1
        
print(cnt)