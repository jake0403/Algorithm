from pprint import pprint
import sys
input = lambda : sys.stdin.readline().strip()

def rotation(x, d, k):
    k %= M
    for i in range(1,N, x):
        # 반시계 방향
        if d:
            L = arr[i][:k]
            R = arr[i][k:]
        # 시계 방향
        else:
            L  = arr[i][:-k]
            R = arr[i][-k:]
        arr[i] = R + L



N, M, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
pprint(arr)
for i in range(T):
    x, d, k  = map(int, input().split())
    rotation(x,d,k)
cnt = 0
avg = 0
for i in range(N):
    avg+= sum(arr[i])
    for j in range(M):
        if arr[i][j]:
            for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr = i + dr
                nc = (j + dc) % M
                if 0<=nr<N and arr[i][j] == arr[nr][nc]:
                    arr[i][j] = arr[nr][nc] = 0
                    cnt+=1
if not cnt:
    for i in range(N):
        for j in range(M):
            pass


