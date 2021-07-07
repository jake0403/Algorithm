T = int(input())
for test_case in range(1, T + 1):
    N, R = map(int, input().split())
    num_list = list(map(int, input().split()))
    max_v = 0
    min_v = sum(num_list)
    for i in range(N - R + 1):
        if max_v < sum(num_list[i:i + R]):
            max_v = sum(num_list[i:i + R])
        if min_v > sum(num_list[i:i + R]):
            min_v = sum(num_list[i:i + R])
    print(f'#{test_case} {max_v-min_v}')

#######################################################################################################################

# window sliding
# 중복된 연산을 피함
Total = int(input())
for tc in range(1, Total + 1):
    # N : 원소의 개수
    # M : 더할 구간의 길이
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    tmp = 0
    # 첫 구간 구하기
    for i in range(M):
        tmp += nums[i]

    max_value = tmp
    min_value = tmp
    # 첫 구간은 제외하고 그 뒤에 남은 구간부터
    for i in range(M, N):
        # 새로운 구간의 합을 간단하게 구할 수 있음
        tmp += nums[i] - nums[i - M]

        if max_value < tmp:
            max_value = tmp
        if min_value > tmp:
            min_value = tmp
    print("# {} {}".format(tc, max_value - min_value))