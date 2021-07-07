# 각 범위 구하는 함수
def charge(N, num_list):
    # 투포인터로 구현하기 위해 start, end 변수 설정
    start = cnt = 0
    end = N-1
    # 각 4등분된 수확량 담을 리스트 생성
    answer = []
    # 총 N 번만 돌아도 됨
    for i in range(N):
        # 시작점과 끝점이 같지 않다는건 수확량이 사이에 있다는 것
        if start != end:
            # 경계선 안에 포함되어 있는 수확량을 다 더해줌
            cnt += sum(num_list[i][start + 1:end])
            # 시작점은 왼쪽에서 오른쪽으로
            start += 1
            # 끝점은 오른쪽에서 왼쪽으로
            end -= 1
        # 시작점과 끝점이 같다는 것은 밭의 정중앙에 도달했다는 뜻
        else:
            # 한 명의 수확량이 끝났으므로 정답에 넣어줌
            answer.append(cnt)
            # 맞은편 밭 수확량 확인하기 위해 cnt 변수 초기화
            cnt = 0
            # 맞은편 변수 구하려면 열 부분을 대체할 변수가 필요(이때부터 꼬이기 시작함)
            z = i+1
            # start 변수가 왼쪽 끝, end 변수가 오른쪽 끝에 도달할 때 까지
            while start != 0 and end != N - 1:
                start -= 1
                end += 1
                cnt += sum(num_list[z][start + 1:end])
                # 위에 i를 대체하기 위해서 z변수 +1 해줌
                z+=1
            answer.append(cnt)
    return answer

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    # 편법 사용
    # 2차원 배열 90도 돌리기
    num_list_col = list(map(list, zip(*num_list)))
    #가로 방향의 수확량 구하기
    row_charge = charge(N, num_list)
    #세로 방향 수확량 구하기
    col_charge = charge(N, num_list_col)
    # 합쳐서 4명의 수확량 리스트 만들기
    answer = row_charge + col_charge
    #for 문 2번 돌릴 힘이 없어서 min/max함수 사용
    max_real = max(answer)
    min_real = min(answer)
    print(f'#{tc} {max_real - min_real}')