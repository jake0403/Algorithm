T = int(input())
# 8방향 탐색
dr = [-1, 0, 1, 0, -1, -1, 1, 1]
dc = [0, 1, 0, -1, -1, 1, 1, -1]
def dfs(r, c, dr, dc, color, index):
    # 탐색하고자 하는 색과 동일하다면
    if othello[r][c] == color:
        for i in range(index):
            # 돌 뒤집기
            othello[change[i][0]][change[i][1]] = color
        return
    else:
        # 동일하지 않으면 그 위치 값 저장
        change[index][0] = r
        change[index][1] = c
    nr = r + dr
    nc = c + dc
    # next row next col 조건 걸고 재귀
    if 0 <= nr < N and 0 <= nc < N:
        if othello[nr][nc] != 0:
            dfs(nr, nc, dr, dc, color, index+1)
        # 위치 저장 값 초기화
        change[index][0] = 0
        change[index][1] = 0

for tc in range(1, T+1):
    N , M = map(int, input().split())
    othello = [[0]*N for x in range(N)]
    # 변경 값 담을 변수
    change = [[0]*2 for _ in range(N)]
    black = 0
    white = 0
    mid = N // 2
    # white 초기 값
    othello[mid][mid] = 2
    othello[mid-1][mid-1] = 2
    # black 초기 값 ( row랑 col 값이 반대로지만 그냥 문제에서 주어진 대로 해결)
    othello[mid-1][mid] = 1
    othello[mid][mid-1] = 1

    # 돌의 개수 만큼 반복
    for i in range(M):
        r, c, color = map(int,input().split())
        r-=1
        c-=1
        # 오델로 값 변경
        othello[r][c] = color

        # 8방향 탐색
        for j in range(8):
            nr = r + dr[j]
            nc = c + dc[j]
            # 칸 수를 안넘어가거나 다음 칸이 비어있지 않다면 탐색
            if 0 <= nr < N and 0 <= nc < N and othello[nr][nc] != 0:
                dfs(nr, nc, dr[j], dc[j], color, 0)

    # 바뀌 오델로에서 흰색 검은색 개수 더하기
    for i in range(N):
        for j in range(N):
            if othello[i][j] == 1:
                black+=1
            elif othello[i][j] == 2:
                white+=1

    print(f'#{tc} {black} {white}')
