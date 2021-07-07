T = int(input())
for tc in range(1,T+1):
    N = int(input())
    snail_arr = [[0]*N for x in range(N)]
    change = 0
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    r = c = 0
    snail_arr[r][c] = 1

    for i in range(2,N**2+1):
        r +=dr[change]
        c +=dc[change]
        snail_arr[r][c] = i
        nr = r + dr[change]
        nc = c + dc[change]
        if 0<= nr < N and 0 <= nc < N and not snail_arr[nr][nc]:
            continue
        if change < 3 :
            change+=1
        else:
            change = 0
    print(f'#{tc}')
    for s in snail_arr:
        print(*s)