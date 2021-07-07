T = int(input())
for tc in range(1, T + 1):
    num_list = list(map(int, input().split()))
    n = len(num_list)

    answer = 0
    for i in range(1, 1 << n):
        total = 0
        for j in range(n):
            if i & (1 << j):
                total += num_list[j]
        if total == 0:
            answer = 1

    print(f'#{tc} {answer}')