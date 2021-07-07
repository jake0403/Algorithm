T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # 학생들 지나갈 복도 번호 담을 변수 => answer
    answer = [0]* 200
    room = [list(map(int, input().split())) for x in range(n)]
    for i in range(n):
        # 출발 지점 방 번호가 도착 지점 방 번호보다 작은 경우
        if room[i][0] < room[i][1]:
            start = (room[i][0]-1)//2
            end = (room[i][1]-1)//2
        # 출발 지점 방 번호가 도착 지점 방 번호보다 큰 경우
        else:
            end = (room[i][0] - 1) // 2
            start = (room[i][1] - 1) // 2
        # 슬라이싱으로 복도 번호 구하기
        for i in range(start, end+1):
            answer[i]+=1
        # answer.append([x for x in range(start, end+1)])
    # 가장 많이 움직이는 학생 순서대로 정렬
    max_count = 0
    for i in answer:
        if max_count < i:
            max_count = i
    print(f'#{tc} {max_count}')