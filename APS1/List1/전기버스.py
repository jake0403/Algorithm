T = int(input())
result = []
for test_case in range(1, T + 1):
    # k : 버스의 최대 이동 가능 거리
    # n : 이동할 거리
    # m : 충전소 개수
    k, n, m = map(int, input().split())

    # 충전소 위치 인덱스 받기
    charge = list(map(int, input().split()))

    # 출발 위치와 종점 위치를 충전소 위치 양 끝에 붙임 ( 충전소까지의 거리(간격)만 파악하면 되니깐 )
    charge_route = [0] + charge + [n]

    # 출발 위치와 첫 번째 충전소, 그리고 충전소끼리의 거리를 구하는 Array를 생성한다.
    run_limit = [(charge_route[x+1]-charge_route[x]) for x in range(len(charge_route)-1)]

    # 충전 횟수 입력 받을 변수 생성
    count = 0

    # 충전소까지의 거리를 바탕으로 for문을 돈다.
    for run in run_limit:

        #충전소까지의 거리 차이가 최대 이동 거리를 넘어간다면
        if run > k:
            #결과에 0을 넣는다.
            result.append(0)
            break
    # 파이썬만의 특징인 for else문으로 break가 되지 않는다면
    # 즉, 거리 차이가 최대 이동거리를 넘지 않는다면,
    else:
        # 최대 이동거리가 이동하면서 감소되어야 하므로 k_limit이라는 변수 생성
        k_limit = k

        # 출발 지점은 이동 횟수에 포함되지 않으므로 전체 이동할 거리에서 -1 한 후, for문을 돈다.
        for i in range(len(run_limit)-1):

            # 만약 내가 이동할 수 있는 거리가 충전소 까지의 거리보다 같거나 크다면
            if k_limit >= run_limit[i]:
                # 내가 이동할 수 있는 거리를 충전소 위치 간격만큼 이동 가능 거리를 빼준다.
                k_limit -= run_limit[i]
                # 그 빼준 값이 그 다음 충전소까지 거리보다 작으면(즉, 앞으로 충전소까지 갈 거리가 이동 가능 거리 수 보다 많이 남았다면)
                if k_limit < run_limit[i+1]:
                    # 이전 충전소에서 충전을 하고 출발을 한다.
                    # 충전을 했으니 이동 가능 거리를 최대 이동 가능 거리 수로 초기화
                    k_limit = k
                    # 충전 횟수 더해주기
                    count+=1
        # 총 충전한 횟수 결과 Array에 저장.
        result.append(count)
    print(f'#{test_case} {result[test_case-1]}')


def backtrackBus(k,n,charge):
    bus_stop = [0] * (n+1)

    #충전소 표시
    for i in charge:
        bus_stop[i] = 1
    bus = 0     # 버스 위치
    ans = 0     # 충전 횟수

    while True :
        # 버스가 이동할 수 있는 만큼 이동을 하자.
        bus+= k
        if bus >= n : break     # 종점에 도착하거나 종점을 지나 더 나아간 경우

        for i in range(bus, bus-k, -1):
            if bus_stop[i]:
                ans+=1
                bus = i
                break
        # 충전기를 못 찾았을 때
        else:
            ans = 0

    return ans