def dfs(r,c,cnt):
    global minV
    if r == N-1 and c == N-1:
        if cnt < minV:
            minV = cnt
    if cnt < minV:
        for dr, dc in [(0,1), (1,0)]:
            nr = r + dr
            nc = c + dc
            if 0<= nr < N and 0 <= nc <N:
                cnt += arr[nr][nc]
                dfs(nr,nc,cnt)
                cnt -= arr[nr][nc]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = arr[0][0]
    minV = 1301
    dfs(0,0,cnt)
    print(f'#{tc} {minV}')