from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

def bfs():
    q = deque([])
    q.append([0,0])
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1

    while q:
        r, c = q.popleft()
        for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            nr, nc = r + dr, c + dc

            if 0<=nr<N and 0<=nc<M and not visited[nr][nc]:
                if cheese[nr][nc] >= 1:
                    cheese[nr][nc]+=1
                else:
                    visited[nr][nc] = 1
                    q.append([nr,nc])


N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]
hour = 0
while True:
    bfs()
    flag = 0

    for i in range(N):
        for j in range(M):
            if cheese[i][j]>=3:
                cheese[i][j] = 0
                flag = 1
            elif cheese[i][j] == 2:
                cheese[i][j] = 1
    if flag:
        hour+=1
    else:
        break
print(hour)
