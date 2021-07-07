T = int(input())
for tc in range(1, T+1):
    frist = input()
    board_listA = list(map(int,input().split()))
    board_listB = list(map(int, input().split()))
    # 주사위 던지는 횟수
    i = 0
    # A 점수
    A_score = 0
    # B 점수
    B_score = 0
    # 우승자는 무승부로 초기화
    winner = "AB"
    # 주사위 10번 던질 횟수 (무승부)
    while i <10:
        # A 주사위 리스트와 B 주사위 리스트 길이 같으므로
        # 주사위 리스트 만큼 loop
        for i in range(len(board_listA)):
            # 첫 번째가 A이면
            if frist == "A":
                # A 먼저 추가
                A_score+= board_listA[i]
                B_score+=board_listB[i]
                # B가 A를 따라 잡았을 경우
                if A_score == B_score:
                    # A 점수 처음 위치로 초기화
                    A_score == 0
                # A가 20점 이상이면
                if A_score >= 20:
                    winner = "A"
                # B가 20점 이상이면
                elif B_score >= 20:
                    winner = "B"
                # 주사위 횟수 count
                i+=1
            # B가 먼저인 경우
            else:
                # B 먼저 더함
                B_score+=board_listB[i]
                A_score+=board_listA[i]
                # A가 B를 따라잡으면
                if A_score == B_score:
                    # B 점수 처음 상태로
                    B_score == 0
                # 승자 확인
                if A_score >= 20:
                    winner = "A"
                elif B_score >= 20:
                    winner = "B"
                # 주사위 횟수 count
                i+=1
    print(f'#{tc} {winner}')