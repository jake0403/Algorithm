T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 1이상 N^2까지의 숫자가 담겨있는 N * N 행렬
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 이동 가능한 방을 담아둘 리스트 생성 => ex) [0,0,0,1,1,0,0,0,1,1,0,0]
    move = [0]*(N**2+1)
    for r in range(N):
        for c in range(N):
            # delta move로 탐색
            for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                nr = r + dr
                nc = c + dc
                # 1차이가 나는 값을 move 인덱스에 1로 채우기
                if 0<= nr < N and 0<= nc < N and arr[r][c]+1 == arr[nr][nc]:
                    move[arr[r][c]] = 1
                    break
    cnt = 1
    maxC = 1
    start = 0
    for i in range(1, N**2+1):
        if move[i]:
            cnt+=1
        else:
            if cnt > maxC:
                maxC = cnt
                start = i-cnt+1
            cnt = 1
    print(f'#{tc} {start} {maxC}')