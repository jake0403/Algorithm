T = int(input())    # 테스트 케이스 수

for tc in range(1, T+1):
    # N 과 M 입력
    N, M = map(int, input().split())
    # Tree를 심을 전체 2차원 배열 생성
    tree_list = [list(map(int, input().split())) for _ in range(N)]

    # 문제 조건 순서대로 비용, 나무 수, 비싼 나무, 비싼 나무 위치
    total = amount = expensive = idx = 0

    # 열 loop
    for i in range(M):
        # 행 loop
        for j in range(N):
            # 나무는 한칸 씩 띄워서 심으므로 짝수번째
            if i % 2 ==0:
                # 나무 수 계산
                amount+=1
                # 총 비용 계산
                total+=tree_list[j][i]
                # 가장 비싼 나무가 전에 있던 열에도 있으면
                # 뒤에 있는 열이 우선이므로 <= 부등호 사용
                if expensive <= tree_list[j][i]:
                    expensive = tree_list[j][i]
                    # 비싼 나무가 있는 위치의 열 저장
                    idx = i+1
    print(f'#{tc} {total} {amount} {expensive} {idx}')
