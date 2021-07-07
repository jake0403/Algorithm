T = int(input())
for tc in range(1, T+1):
    r , n = map(int, input().split())
    answer = ''
    #word 2차원 배열 담을 변수 설정
    word = [list(map(str, input())) for _ in range(r)]
    # 정사각형이므로 r 번씩 반복 (행,열)
    for i in range(r):
        #하지만 열은 n개의 개수인 펠린드롬을 찾는 것이기 때문에 r-n+1
        for j in range(r-n+1):
            row = ''
            col = ''
            #총 길이만큼 단어 수 더해가서
            for l in range(n):
                row+=word[i][j+l]
                col+=word[j+l][i]
            #거꾸로 해도 같은지 비고
            if row == row[::-1] and len(row) == n:
                answer = row
            # 세로 비교
            elif col == col[::-1] and len(row)==n:
                answer = col
        if answer: break
    print(f'#{tc} {answer}')
