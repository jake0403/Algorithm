T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_arr = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    chemical = []
    # 행렬 전체 돌면서 0이 아닌 숫자가 나오면 count
    # count = 부분 행렬의 row 길이
    # 같은 count의 개수  = 부분 행렬의 col 길이
    for i in range(N):
        for j in range(N):
            if num_arr[i][j] != 0:
                cnt+=1
            else:
                if cnt:
                    chemical.append(cnt)
                cnt = 0
        if cnt:
            chemical.append(cnt)
        cnt = 0
    # 정렬을 하면 부분 행렬의 col row 개수 쉽게 알 수 있음
    chemical.sort()
    # ex) [3,3, 4,4,4, 5,5,5,5]
    answer = []
    # 부분 행렬 개수 1로 초기화
    m_n = 1
    # 첫 번째 값 먼저 넣어줌
    answer.append([chemical.count(chemical[0]), chemical[0]])
    # 뒤에 값과 다른 경우 다른 부분행렬
    for c in range(len(chemical)-1):
        if chemical[c] != chemical[c+1]:
            # 개수 더해주고
            m_n+=1
            # 행 개수 파악
            row = chemical.count(chemical[c+1])
            # 부분 행렬 행 렬 구분해서 넣어주기
            answer.append([row, chemical[c+1]])
    # 문제 조건에 따른 정렬
    answer.sort(key= lambda x: (x[0]*x[1], -x[1]))
    ans = []
    for i in answer:
        for j in i:
            ans.append(j)
    print(f'#{tc}',m_n, *ans)