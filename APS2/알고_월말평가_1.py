def victim(r,c):
    global exploded, kill
    # 대각으로 이동하는 delta
    for dr, dc in [(1,1), (1,-1), (-1,-1), (-1,1)]:
        # 폭발력 count 하는 변수 생성
        p = 0
        # 다음에 이동할 델타 값을 위해 초기화
        nr = nc = 0
        # 폭발력을 만족할 때까지 while 문
        while p < power:
            # delta move가 양수이면 폭발력을 더해줘야함
            # 그래야지 그 다음 칸으로 이동 가능
            if dr >= 0 :
                nr = r + dr + p
            # 음수이면 빼줘야함
            # 폭발력 만큼 왼쪽 또는 위로 이동해야하기 때문
            else:
                nr = r + dr - p
            if dc >= 0 :
                nc = c + dc + p
            else:
                nc = c + dc - p
            # 다음으로 이동할 때 범위를 벗어나지 않거나 이미 폭발하지 않은 곳만 탐색
            if 0<= nr <N and 0<= nc < N and exploded[nr][nc] != 1:
                exploded[nr][nc] = 1
                kill += arr[nr][nc]
            # 폭발력 정보 업데이트
            p += 1


T = int(input(()))
for tc in range(1, T+1):
    # N : 행렬 개수
    # B : 폭탄 개수
    N, B = map(int, input().split())
    # 적군 수 담겨있는 array
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 폭발한 정보 즉 이미 피해를 입은 적군 정보 담을 array ( 전체 정보 담기 때문에 for 문 밖에)
    exploded = [[0] * N for _ in range(N)]
    # 피해 입은 적군 수 (얘도 전체 정보 담기 때문에)
    kill = 0
    # 폭탄 개수만큼 반복
    for b in range(B):
        # 폭탄 터지는 위치 및 폭발력 정보
        bomb = list(map(int, input().split()))
        power = bomb[-1]
        bomb = bomb[:-1]
        # 처음 폭탄 터진 곳 죽은 적군 수 더하기
        kill += arr[bomb[0]][bomb[1]]
        # 폭탄 터진 위치 저장하는 곳 1로 변환
        exploded[bomb[0]][bomb[1]] = 1
        # 반복하며 함수 실행
        victim(bomb[0], bomb[1])
    print('#{} {}'.format(tc, kill))
