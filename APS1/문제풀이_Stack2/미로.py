def f(si, sj, N):   # 방문한 칸을 벽으로 메우면서 탐색하는 코드1 (dfs -> stack)
    stack = []
    # visited는 통로를 벽으로 만드는 방법으로 해결
    stack.append((si, sj))
    # 방문한 통로는 벽으로 바꿈
    maze[si][sj] = 1

    # 스택이 비어있지 않으면 ( 아직 방문할 곳이 남아 있으면)
    while stack:
        # i, j 칸 방문
        i, j = stack.pop()
        # 목적지인 경우 벽으로 메꾸는 경우 여기서 확인 불가
        # if maze[i][j] == 3:
        #     return 1
        # i, j의 주변 칸 인덱스
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = i + di
            nj = j + dj
            # 미로를 벗어나지 않고 벽이 아니면
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1:
                # 목적지인 경우 벽으로 메꾸지 않고 종료
                if maze[ni][nj] == 3:
                    return 1
                else:
                    # 탐색 목록에 추가하고
                    stack.append((ni, nj))
                    # 벽으로 메꿈
                    maze[ni][nj] == 1
    return 0    # 도착하지 못하는 경우

def f2(si, sj, N):
    stack = []
    visited = [[0]*N for _ in range(N)]
    stack.append(si, sj)
    visited[si][sj] = 1
    while stack:
        i , j = stack.pop()
        if maze[i][j] == 3:
            return 1
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = i + di
            nj = j + dj
            # 미로를 벗어나지 않고 벽이 아니면
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj]==0:
                stack.append((ni, nj))
                visited[ni][nj] = 1
    return 0
def dfs_maze(i, j, N):
    if maze[i][j] == 3:
        return 1
    else:
        visited[i][j] = 1
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and visited[ni][nj] ==0:
                if dfs_maze(ni,nj,N):
                    return 1
        return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j   # 출발 칸 찾기

    print(f'#{tc} {f(si,sj, N)}')