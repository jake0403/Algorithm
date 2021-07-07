T = int(input())
for tc in range(1,T+1):
    N, p = map(int,input().split())
    flies = [list(map(int,input().split())) for _ in range(N)]

    #파리채 크기로 row랑 column 생성
    r = [x for x in range(0,p)]
    c = [y for y in range(0,p)]
    max_kill = 0
    # 전체 array 크기 반복
    for i in range(N-p+1):
        for j in range(N-p+1):
            sum_kill = 0
            #파리채 크기 돌면서 값 더하기
            for x in r:
                for y in c:
                    sum_kill+= flies[i+x][j+y]
            #최대값 구하기
            if max_kill < sum_kill:
                max_kill = sum_kill
            sum_kill = 0
    print(f'#{tc} {max_kill}')