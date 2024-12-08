n, s = map(int,input().split())
l = list(map(int, input().split()))

left = 0
partial_sum = 0
min_length = 987654321

for right in range(n):
    partial_sum += l[right]
    if partial_sum >= s:
        min_length = min(min_length,right-left+1)
    while partial_sum - l[left] >= s:
        partial_sum -= l[left]
        left += 1
        min_length = min(min_length,right-left+1)
print(min_length if min_length != 987654321 else 0)