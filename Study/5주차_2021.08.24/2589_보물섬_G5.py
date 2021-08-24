from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()


def bfs(r,c):
    q = deque()
    q.append([r,c])
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1
    dist = 0
    while q:
        r,c = q.popleft()
        for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<M and tmap[nr][nc] == "L" and not visited[nr][nc]:
                q.append([nr,nc])
                visited[nr][nc] = visited[r][c] + 1
                dist = max(dist, visited[nr][nc])
    return dist-1

N, M = map(int, input().split())
tmap = [list(input()) for _ in range(N)]


max_route = 0
for i in range(N):
    for j in range(M):
        if tmap[i][j] == 'L':
            v = bfs(i,j)
            max_route = max(max_route,v)
print(max_route)