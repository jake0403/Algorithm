T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    for i in range(1, 1 << 12):
        total = 0
        count = 0
        answer = 0
        num_list = [i for i in range(1,12+1)]
        for j in range(12):
            if i & (1 << j):
                count+=1
                total+=num_list[j]
            if count == N and total == K:
                answer+=1
    print(f'{tc} {answer}')