T = int(input())
for tc in range(1, T+1):
    N, P = map(int,input().split())
    cheese = list(map(int, input().split()))
    # [(7, 1), (2, 2), (6, 3), (5, 4), (3, 5)] 치즈 양과 피자 순서
    cheese = [[pizza, i+1] for i, pizza in enumerate(cheese)]
    # 화덕에 들어간 피자 = queue
    queue = cheese[:N]
    # 남은 피자
    cheese = cheese[N:]
    # 화덕에 남은 피자가 1개일 때까지 반복
    while len(queue) != 1:
        #꺼내고
        c, p = queue.pop(0)
        # 치즈 녹은 거 확인
        c//=2
        # 치즈가 안 녹았으면 다시 화덕에 넣기
        if c:
            queue.append((c,p))
        # 녹았다면
        else:
            # 남은 피자 확인 후 화덕에 넣기
            if cheese: queue.append(cheese.pop(0))
    print(f'#{tc} {queue[-1][1]}')