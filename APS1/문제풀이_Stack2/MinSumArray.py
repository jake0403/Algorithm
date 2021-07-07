# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     num_list = [list(map(int,input().split())) for _ in range(N)]
#     answer = 0
#     dp = [0]*N
#     for i in range(N):
#         min_num = 10
#         for j in range(N):
#             if num_list[i][j] < min_num:
#                 if dp[j] == 1:
#                     continue
#                 else:
#                     if min_num == 10:
#                         pass
#                     else:
#                         dp[num_list[i].index(min_num)] = 0
#                     min_num = num_list[i][j]
#                     dp[j] = 1
#         answer+=min_num
#
#     print(f'#{tc} {answer}')
def dfsMin(col):
    global isMin, answer
    # 계속 더한 값이(isMin) 전에 더한 값 보다 크다면 탐색할 필요 없음
    if answer < isMin:
        return
    # 탐색을 다 마친 경우
    if col == N:
        # answer 보다 현재 다 더한 값이 최소값이면
        if isMin < answer:
            # 값 변환
            answer = isMin
            return
    else:
        # 행을 다 돌면서 모든 경우의 수 다 더함
        # 처음엔 값이 다 0인 대각선 방향으로 값을 검색 후
        # 재귀이므로 뒤에서 부터 다시 원상복구 후 값을 비교
        for row in range(N):
            # 방문하지 않은 곳이면
            if not dp[row]:
                # 체크
                dp[row] =1
                #값 누적
                isMin+= num_list[col][row]
                # 재귀로 탐색
                dfsMin(col+1)
                # 방문한 위치 원상복구
                dp[row] = 0
                # 값 원상복구
                isMin -= num_list[col][row]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    # 배열에서 최대 값이 될 수 있는 값은 90이기 때문
    isMin , answer = 0, 99
    # 방문한 열 체크
    dp = [0] * N
    dfsMin(0)
    print(f'#{tc} {answer}')
