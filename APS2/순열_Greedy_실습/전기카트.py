# i : 방문지 번호
# n : 총 전체 방문지 수
# k : 방문 순서
# s : i에 도착할 때까지 사용한 에너지
def f(i, n, k, s):
    global minV
    if n == k:
        # 마지막 방문지에서 사무실로 가는 비용 추가
        if minV > s+e[i][0]:
            minV = s+e[i][0]
    elif s >= minV:
        return
    else:
        for j in range(n):
            if visited[j] == 0:
                visited[j] = 1
                f(j,n, k+1, s+e[i][j])
                visited[j] = 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    visited[0] = 1
    minV = 10000
    f(0, N, 1, 0)
    print(f'#{tc} {minV}')