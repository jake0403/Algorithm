def hikingRoute(r, c, k, cnt):
    global visited, ans
    if cnt > ans :
        ans = cnt
    visited[r][c] = 1

    for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
        nr = r + dr
        nc = c + dc
        if visited[nr][nc] == 0 and 0 <= nr < N and 0:
            if arr[nr][nc] < arr[r][c]:
                hikingRoute(nr, nc, k, cnt+1)
                visited[nr][nc] = 0

            elif arr[r][c] - arr[nr][nc] <= k:
                    temp = arr[nr][nc]
                    # arr[nr][nc] =
                    hikingRoute(nr, nc, 0, cnt+1)
                    visited[nr][nc] = 0



T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxH = 0
    visited = [[0]*N for _ in range(N)]
    # 가장 높은 등산로 찾는 과정
    for i in arr:
        maxH = max(maxH, max(i))
    ans = 0
    cnt = 0
