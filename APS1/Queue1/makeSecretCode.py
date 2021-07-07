for tc in range(1, 11):
    input()
    numArray = list(map(int, input().split()))
    cycle = 1

    while True:
        p = numArray.pop(0)
        # 감소한 값이 0이하이면
        if p - cycle <= 0:
            numArray.append(0)
            break
        # 0보다 크면
        else:
            numArray.append(p - cycle)
        cycle+=1
        # cycle 5보다 크면 초기화
        if cycle > 5 :
            cycle = 1
    numArray = [str(i) for i in numArray]
    numArray = ' '.join(numArray)
    print(f'#{tc} {numArray}')