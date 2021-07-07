T = int(input())
for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    guest = list(map(int, input().split()))
    guest.sort()
    answer = "Possible"
    # 손님 순서, 남은 붕어빵 초기화
    idx = having = 0
    # 가장 늦게 오는 손님 시간만큼 반복
    for g in range(guest[-1] + 1):
        # 시간이 0초 아닐 때
        if g != 0:
            # 시간대가 붕어빵이 구워질 시간이라면
            if g % m == 0:
                # 붕어빵 추가
                having += k
        #시간이 손님 도착 시간이라면
        if g == guest[idx]:
            # 붕어빵이 없다면
            if having ==0:
                answer = 'Impossible'
                print(f'#{tc} {answer}')
                break
            # 붕어빵이 있다면
            else:
                # 붕어빵 감소
                having-=1
                # 손님 변경
                idx+=1

        if g == guest[-1] and having !=0:
            print(f'#{tc} {answer}')
