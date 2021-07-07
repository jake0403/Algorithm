def minCost(idx, cost):
    global minC, visited

    if cost >= minC:
        return
    if idx == N :
        if minC > cost:
            minC = cost
    else:
        for i in range(N):
            if visited[i] != 1:
                visited[i] = 1
                minCost(idx+1, cost+arr[idx][i])
                visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    minC = 22500
    minCost(0,0)
    print(f'#{tc} {minC}')

