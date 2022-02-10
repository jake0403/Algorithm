import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()

N, M = map(int, input().split())
field = [list(input()) for _ in range(M)]

def power(r,c, color):
    q = deque([])
    q.append([r,c])
    field[r][c] = 0
    cnt = 1

    while q:
        r, c = q.popleft()
        for dr, dc in ([0,1],[1,0],[0,-1], [-1,0]):
            nr, nc = r + dr, c + dc
            if field[nr][nc] == color and 0<=nr<N and 0<=nc<M:
                q.append([nr,nc])
                cnt+=1
                field[nr][nc] = 0
    if cnt > 1:
        return cnt**2
    else:
        return 1
w = b = 0
for i in range(N):
    for j in range(M):
        if field[i][j] == 'W':
            w+=power(i,j,'W')
        elif field[i][j] == 'B':
            b+=power(i,j,'B')
print(w, b)