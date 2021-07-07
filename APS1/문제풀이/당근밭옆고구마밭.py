T = int(input())
for tc in range(1, T+1):
    N = int(input())
    swp = list(map(int, input().split()))

    # 긴 줄기 개수, 가장 긴 줄기 고구마 개수 초기화
    count = 1
    result =[]
    for i in range(N - 1):
        if swp[i] < swp[i+1]:
            count+=1
        else:
            # 연속 증가 값 저장
            if count > 1:
                result.append(swp[i-count : i+1])
                count = 0
        # 마지막 값 추가
    if count > 1:
        result.append(swp[N-count-1:])
    max_len = 1
    max_sum = 0
    for r in result:
        if max_len < len(r):
            max_len = len(r)
            max_sum = sum(r)
        elif max_len == len(r):
            max_sum = sum(r)
    print(f'#{tc} {len(result)} {max_sum}') if max_sum > 1 else print(f'#{tc} 0 0')