import sys
input = lambda : sys.stdin.readline().strip()

N = int(input())
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(input())

tmp = arr[0]
for i in range(1,N):
    for j in range(len(tmp)):
        if tmp[j] != arr[i][j]:
            tmp[j] = '?'
print(''.join(tmp))