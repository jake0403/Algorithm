T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    answer = []
    for i in range(N):
        # i가 중간 값보다 작거나 같으면
        if i <= N//2:
            # i에 따른 연산만큼 추가
            answer.append(farm[i][N//2 - i: N//2 +(i+1)])
        # i가 크면
        else:
            # 그에 따른 연산
            answer.append(farm[i][i-N//2 : (N -i)+N//2])
    result = [sum(a) for a in answer]
    print(f'#{tc} {sum(result)}')