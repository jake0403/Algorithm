T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    # 방문 체크
    visited = [[0]*N for _ in range(N)]
    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j
    # 시작점 방문했다고 체크
    visited[si][sj] = 1
    # queue에 시작점 넣기
    queue = [[si, sj]]
    # 여려 경로 나올 수 있으므로 answer 객체 생성
    answer = []
    while queue:
        i, j = queue.pop(0)
        # delta move 통해 열린 길 탐색
        for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and maze[ni][nj] != 1:
                # 방문한 거리 세기 위해서 전에 방문했던 값 누적 합
                visited[ni][nj] = 1 + visited[i][j]
                # queue에 다음 방문할 index 값 넣기
                queue.append([ni,nj])
                # 다음 검색할 값이 3이라면
                if maze[ni][nj] == 3:
                    # answer에 거리 값 넣어주기
                    answer.append(visited[i][j])
                    # 큐 초기화
                    queue = [[si,sj]]
    # 미로 탈출 실패
    if not answer:
        answer = 0
    # 그게 아니라면 최소 탈출 경로 반환
    else:
        answer = min(answer)-1

    print(f'#{tc} {answer}')