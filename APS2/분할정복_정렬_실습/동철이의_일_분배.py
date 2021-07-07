def work(idx, success):
    global visited, maxS
    if idx == N:
        if maxS < success:
            maxS = success
        return
    elif maxS >= success:
        return
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                work(idx+1, success * float(arr[idx][i] / 100))
                visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    maxS = 0
    work(0,1)
    print(f'#{tc} {format(maxS*100, "6f")}')

