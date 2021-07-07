T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    num_list = list(map(int, input().split()))
    min_num = 1000001
    max_num = 0

    for i in num_list:
        if min_num > i:
            min_num = i
        if max_num < i:
            max_num = i
    print(f'#{test_case} {max_num-min_num}')