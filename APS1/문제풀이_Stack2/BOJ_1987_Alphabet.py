# 주어진 알파벳 표에서 말이 최대 이동할 수 있는 거리 구하는 문제
# 단 지나간 알파벳과 같은 알파벳 자리는 지나갈 수 없음.
# def countPath(si,sj):
#     stack = []
#     cnt = 1
#     max_count = 0
#     # 방문한 장소 체크 리스트 생성
#     visited = [[0]*C for _ in range(R)]
#     # 스택에 첫 번째 방문 요소 담기
#     stack.append((si, sj))
#     # 방문한 리스트에 체크
#     visited[si][sj] = 1
#     alpha = []
#     alpha.append(board[si][sj])
#
#     while stack:
#         i, j = stack.pop()
#         if board[i][j] in alpha:
#             if max_count < cnt :
#                 max_count = cnt
#         for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
#             ni = i + di
#             nj = j + dj
#             if 0<= ni <R and 0 <= nj < C and visited[ni][nj] == 0 and board[ni][nj] not in alpha :
#                 stack.append((ni,nj))
#                 alpha.append(board[ni][nj])
#                 cnt+=1
#                 visited[ni][nj] = 1
#     return max_count

def dfs_count(i,j,ans):
    global answer
    answer = max(ans, answer)
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni = i + di
        nj = j + dj
        if 0 <= ni < R and 0 <= nj < C and visited[board[ni][nj]] == 0:
            visited[board[ni][nj]] = 1
            dfs_count(ni, nj, ans+1)
            visited[board[ni][nj]] = 0

R , C = map(int,input().split())
board = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(R)]
answer = 0
visited = [0] * 26
visited[board[0][0]] = 1
dfs_count(0, 0, 1)
print(answer)
#print(countPath(0,0))