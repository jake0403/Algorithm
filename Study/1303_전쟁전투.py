from collections import deque
import sys
input = sys.stdin.readline

def findSoliders(r,c, team):
    power = 1
    q = deque()
    q.append([r,c])
    visited[r][c] = 1
    while q:
        r,c = q.popleft()
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<M:
                if not visited[nr][nc] and field[nr][nc] == team:
                    q.append([nr,nc])
                    power+=1
                    visited[nr][nc] = 1
    return power



M, N = map(int, input().split())

field = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
white = blue = 0

for i in range(N):
    for j in range(M):
        if field[i][j] == 'W' and not visited[i][j]:
            white+= findSoliders(i, j, 'W')**2
        elif field[i][j] == 'B' and not visited[i][j]:
            blue+=findSoliders(i, j,'B')**2

print(white, blue)