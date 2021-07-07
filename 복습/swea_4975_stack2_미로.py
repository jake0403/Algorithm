from collections import deque
def bfs(sr,sc):
    visited[sr][sc] = 1
    q = deque([[sr,sc]])
    while q:
        r, c = q.popleft()
        for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
                if maze[nr][nc] == 3:
                    return 1
                elif maze[nr][nc] == 0:
                    q.append([nr,nc])
                    visited[nr][nc] = 1
    return 0

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if maze[r][c] == 2:
                sr, sc = r, c
    print(f'#{tc} {bfs(sr,sc)}')