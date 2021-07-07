from collections import deque
def bfs(r,c):
    q = deque()
    q.append([r,c])
    fuel = 0
    while q:
        r,c = q.popleft()
        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] > arr[nr][nc] - arr[r][c] + 1:
                    visited[nr][nc] = arr[nr][nc] - arr[r][c] + 1 + visited[r][c]
                    q.append([nr,nc])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    INF = 10000
    visited = [[INF]*N for _ in range(N)]
    visited[0][0] = 0
    bfs(0,0)
    print(arr[N-1][N-1])
