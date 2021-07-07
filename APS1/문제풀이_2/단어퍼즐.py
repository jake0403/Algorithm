T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int,input().split())) for _ in range(N)]     # 퍼즐 배열
    answer = 0      # 정답 변수
    for i in range(N):
        count_row = 0   # 가로 개수 셀 변수
        count_col = 0   # 세로 개수 셀 변수
        for j in range(N):
            if puzzle[i][j] == 1:       # 1이면 count
                count_row+=1
                if j == N-1 and count_row ==K:  # j값이 마지막이면 count 체크
                    answer+=1
            else:
                if count_row == K:
                    answer+=1
                count_row= 0
            # 한 반복문에서 column 값도 확인
            if puzzle[j][i] ==1:
                count_col+=1
                if j == N-1 and count_col == K:
                    answer+=1
            else:
                if count_col == K:
                    answer+=1
                count_col = 0

    print(f'{tc} {answer}')



