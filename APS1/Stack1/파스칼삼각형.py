T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    # 파스칼 총 길이만큼 2차원 배열 생성
    stack = [[0]*x for x in range(1,n+1)]
    # 초기값 지정
    stack[0][0] = 1
    # 값 더해줄 변수 생성
    temp = [1]
    for i in range(1,len(stack)):
        # 값 넣어줄 위에 삼각형 라인 길이 만큼 반복
        for j in range(len(stack[i-1])):
            top = temp.pop(0)
            stack[i][j]+=top
            stack[i][j+1]+=top
        if i != len(stack):
            # temp 변수에 저장 된 값 넣어주기
            for k in stack[i]:
                temp.append(k)
    print(f'#{tc}')
    for s in stack:
        print(*s)
