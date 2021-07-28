T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_arr = list(map(int, input().split()))

    min_num = 1000000
    max_num = 0
    for i in range(N-M+1):
        max_num = max(max_num, sum(num_arr[i:i+M]))
        min_num = min(min_num, sum(num_arr[i:i+M]))

    print(f'#{tc} {max_num - min_num}')