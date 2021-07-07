def dfs(r,c):
    if r == er and c == ec:
        return 1
    if visited[r][c] != -1:
        return visited[r][c]
    visited[r][c] = 0
    for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < M and arr[r][c] > arr[nr][nc]:
            visited[r][c] += dfs(nr,nc)
    return visited[r][c]

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
er, ec = N-1, M-1
print(dfs(0,0))
