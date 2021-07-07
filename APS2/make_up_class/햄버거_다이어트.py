'''
test_case
1
5 1000
100 200
300 500
250 300
500 1000
400 400
'''
# 장훈이의 높은 선반과 비슷한 문제
# 현재 점수와 남은 점수로
def delicious(idx, score, kcal, remain_score):
    global best_score
    # 백트래킹
    # 칼로리가 조건을 넘지 않고, 현재 점수와 더한 점수가 best_score 보다 작지 않아야 함
    # 뒤에 조건이 없으면 남은 점수를 빼줄 때 계속 빼줘서 음수 값이 나옴
    if kcal > L  or score + remain_score < best_score :
        return
    # 재료를 전부 다 돌았으면
    if idx == N:
        # 조건이 더 좋으면 점수 바꿈
        if best_score < score:
            best_score = score
        return
    # 그게 아니라면 재귀
    else:
        # 재료 추가했을 때와 추가하지 않았을 때 탐색
        # 사용 했던 사용하지 않았던 남은 재료 파악
        delicious(idx+1, score + ingre[idx][0], kcal + ingre[idx][1], remain_score - ingre[idx][0] )
        delicious(idx+1, score, kcal, remain_score - ingre[idx][0])



T = int(input())
for tc in range(1, T+1):
    # N: 재료 수
    # L : 칼로리 제한
    N, L = map(int, input().split())
    ingre = [list(map(int, input().split())) for _ in range(N)]
    best_score = 0
    remain_score = sum([ingre[x][0] for x in range(N)])
    delicious(0, 0, 0, remain_score)
    print(f'#{tc} {best_score}')