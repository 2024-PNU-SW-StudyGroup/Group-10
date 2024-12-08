import sys,math
x,y,d,t=map(int,sys.stdin.readline().split())
answer=math.sqrt((x**2)+(y**2))
base_distance=answer
count=float((int(base_distance//d)) + 1)
if count<=2 :
    count=2
print(min(answer, t+ abs(base_distance - d) , float(count*t), (count-1)*t+abs(base_distance-(count-1)*d) ))
