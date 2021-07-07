def hamburger(cnt, total, kcal):
    global score
    # 지정 칼로리 초과 시 반환
    if kcal > L:
        return
    # 기존 점수보다 높으면 최대값인 score로 update
    if score < total:
        score = total
    # 재료 다 사용했으면 반환
    if cnt == N:
        return
    # 점수, 칼로리 지정
    t, k = ingre[cnt]
    # 추가 재료 사용했을 경우
    hamburger(cnt+1, total+t, kcal+k)
    # 재료 사용하지 않았을 경우
    hamburger(cnt+1, total, kcal)


T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    ingre = [list(map(int,input().split())) for _ in range(N)]
    score = 0
    hamburger(0,0,0)
    print(f'#{tc} {score}')
