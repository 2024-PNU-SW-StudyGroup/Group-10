import sys
input = sys.stdin.readline

n,k = map(int, input().split())
lis = list(map(int,input().split()))
cur_sum = sum(lis[:k])
sum_l = [cur_sum]
for i in range(n-k):
    cur_sum += (lis[i+k]-lis[i])
    sum_l.append(cur_sum)
print(max(sum_l))
    