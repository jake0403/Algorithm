T = int(input())

for tc in range(1, T+1):
    n = int(input())
    num_list = list(map(int, input().split()))

    # 버블 정렬은 두 개씩 비교하니 전체 길이 - 2 + 1임 따라서 n-1
    for i in range(n-1,0,-1):
        # 정렬된 값은 빼고 반복 횟수가 줄어들기 때문에 i 만큼 반복
        for j in range(i):
            # 작은 값이 앞에 오게 정렬해줌
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    num = [str(n) for n in num_list]
    num = ' '.join(num)
    print(f'#{tc} {num}')