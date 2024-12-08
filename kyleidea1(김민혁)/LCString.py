import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

matrix_1 = [0]*(len(b)+1)
matrix_2 = matrix_1[:]

maxx = []
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1] == b[j-1]:
            if i%2 == 1:
                matrix_2[j] = matrix_1[j-1]+1
            else:
                matrix_1[j] = matrix_2[j-1]+1
        else:
            if i % 2 == 1:
                matrix_2[j] = 0
            else:
                matrix_1[j] = 0
    maxx.append(max(matrix_2) if i%2 == 1 else max(matrix_1))
print(max(maxx))