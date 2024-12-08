n = int(input())
l = list(map(int,input().split()))
l.sort()
cnt = 0

for i in range(n):
    target = l[i]
    left = 0
    right = n-1 # 투포인터에서, r은 뒤에서부터 옴!
    
    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
        
        cur_sum = l[left]+l[right]

        if cur_sum == target:
            cnt += 1
            break # 찾았으면 넘어가기
        elif cur_sum < target:
            left += 1
        else:
            right -= 1

print(cnt)