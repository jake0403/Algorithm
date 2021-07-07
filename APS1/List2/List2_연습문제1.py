T = int(input())
for tc in range(1, T+1):
    N  = int(input())
    num_arr = [list(map(int, input().split())) for x in range(N)]
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    total = 0
    for r in range(N):
        for c in range(N):
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N:
                    sub = num_arr[r][c] - num_arr[nr][nc]
                    total+=sub if sub > 0 else -sub
    print(f'#{tc} {total}')