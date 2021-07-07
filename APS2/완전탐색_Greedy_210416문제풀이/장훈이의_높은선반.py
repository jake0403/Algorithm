def backtrack(i, wh, rwh):
    global minH
    # 백트래킹 ( 현재 더한 탑의 높이와 선반의 차이가 그전 값 보다 크다면 )
    # 더하고 있는 탑들이 선반 높이보다 낮으면 (min 값을 구하는 조건이기 때문에 필요)
    if minH < wh - H or wh + rwh < H:
        return
    # 마지막 값이거나 선반이 닿을 탑이라면
    if i == N or wh > H:
        if minH > wh - H:
            minH = wh - H
    else:
        backtrack(i+1, wh, rwh - worker[i])
        backtrack(i+1, wh + worker[i], rwh - worker[i])

T = int(input())
for tc in range(1, T+1):
    N, H = map(int, input().split())
    worker = list(map(int,input().split()))
    minH = 200000
    wh = 0
    rwh = sum(worker)
    backtrack(0, wh, rwh)
    print(f'#{tc} {minH}')

