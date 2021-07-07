for i in range(1,11):
    tc = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]
    dr = [-1, 0, 0]
    dc = [0, -1, 1]
    change = 0
    for end in range(100):
        if array[99][end] == 2:
            c = end
    r = 99
    # 끝 지점 2인 사다리 부터 시작
    while r >0:
        r+=dr[change]
        c+=dc[change]
        #내려가다 왼쪽에 1이 있으면 이동
        if 0 < c and array[r][c-1] == 1:
            change = 1
            while 0 < c and array[r][c-1] == 1:
                r+=dr[change]
                c+=dc[change]
            change = 0
        #내려가다 오른쪽에 1이 있으면 이동
        elif c+1 < 100 and array[r][c+1] == 1:
            change = 2
            while c+1<100 and array[r][c+1] ==1:
                r+=dr[change]
                c+=dc[change]
            change = 0
    print(f'#{tc} {c}')


