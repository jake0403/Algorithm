from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

def findTrash(r,c):
    q = deque()
    q.append([r,c])
    arr[r][c] = 0
    cnt = 1
    while q:
        r, c = q.popleft()
        for dr, dc in [(0,1), (1,0), (-1,0),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 1:
                cnt+=1
                q.append([nr,nc])
                arr[nr][nc] = 0
    return cnt


N, M, F = map(int, input().split())

arr = [[0]*M for _ in range(N)]
biggest = 0
for i in range(F):
    r,c = map(int, input().split())
    arr[r-1][c-1] = 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            biggest = max(biggest, findTrash(i,j))
print(biggest)