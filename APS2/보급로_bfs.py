from collections import deque
def bfs(r,c):
    q = deque([])
    q.append([r,c])
    while q:
        r,c = q.popleft()
        for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            nr = r + dr
            nc = c + dc
            if 0<= nr < N and 0 <= nc < N:
                if visited[nr][nc] > visited[r][c] + arr[nr][nc]:
                    visited[nr][nc] = visited[r][c] + arr[nr][nc]
                    q.append([nr,nc])
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[9999]*N for _ in range(N)]
    visited[0][0] = 0
    bfs(0,0)
    print(f'#{tc} {visited[N-1][N-1]}')
