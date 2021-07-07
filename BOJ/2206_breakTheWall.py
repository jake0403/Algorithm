from collections import deque
# def bfs(i,j):
#     chance = 1
#     q = deque()
#     q.append([i,j])
#     visited[i][j] = 1
#     while q:
#         i, j = q.popleft()
#         for di, dj in [(0,1), (1,0), (-1,0), (0,-1)]:
#             ni = i + di
#             nj = j + dj
#             if chance and 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and wall[ni][nj] == 1:
#                 wall[ni][nj] == 0
#                 chance-=1
#                 q.append([ni, nj])
#                 visited[ni][nj] = visited[i][j] + 1
#             elif 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and wall[ni][nj] == 0:
#                 visited[ni][nj] = visited[i][j] + 1
#                 q.append([ni, nj])
#     if visited[N-1][M-1]:
#         return visited[N-1][M-1]
#     else:
#         return -1

def bfs1(i,j,k):
    q = deque()
    visited[i][j][k] = 1
    q.append([i,j,k])

    while q:
        i, j, k = q.popleft()
        for di, dj in [(0,1), (1,0), (-1,0), (0,-1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M:
                # 벽을 부수지 않고 탐색 했을 경우
                if wall[ni][nj] == 0 and visited[ni][nj][k] == -1:
                    q.append([ni,nj,k])
                    visited[ni][nj][k] = visited[i][j][k] + 1
                # 벽을 부수고 탐색 했을 경우
                elif k == 0 and wall[ni][nj] == 1 and visited[ni][nj][1] == -1:
                    q.append([ni,nj,1])
                    visited[ni][nj][1] = visited[i][j][k] + 1


N , M = map(int, input().split())
wall = [list(map(int, input())) for _ in range(N)]
# 벽을 부수고 갔을 때와 아닐 때를 확인하기 위해서 3차원 리스트 생성
visited = [[[-1]*2 for _ in range(M)] for _ in range(N)]
bfs1(0,0,0)
result1, result2 = visited[N-1][M-1][0], visited[N-1][M-1][1]
if result1 != -1 and result2 == -1:
    print(result1)
elif result1 == -1 and result2 != -1:
    print(result2)
else:
    print(min(result1,result2))