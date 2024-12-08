import sys
from collections import deque
input = sys.stdin.readline

T,length,L = map(int,input().split())
truck = deque(list(map(int,input().split())))
bridge = deque()

bridge.append([truck[0],1]) # 첫 트럭 올리기
weight_sum = truck[0] # 현재 적재
time = 1 # 지난 시간
print(bridge)

while truck and bridge:
    tw,pos = bridge[0]
    t = truck.popleft()
    if weight_sum+t <= L:
        bridge.append([t,1])
        weight_sum += t
        time += 1
    else:
        while weight_sum+t > L:
            cur_t,cur_pos = bridge.popleft()
            weight_sum -= cur_t
        for bt,pos in bridge:
            pos += cur_pos
        time += cur_pos
    print(time)


