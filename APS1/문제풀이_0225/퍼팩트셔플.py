T = int(input())
for tc in range(1, T+1):
    n = int(input())
    card = list(input().split())
    answer = []
    # 짝수일 때
    if n % 2 == 0:
        A = card[:n//2]
        B = card[n//2:]
    # 홀수일 때 앞에 카드 A 가 한 개 더 가져감
    else:
        A = card[:n//2+1]
        B = card[n//2+1:]
    for i in range(len(B)):
        answer.append(A[i])
        answer.append((B[i]))
    # 홀수이면 A가 1개 더 남아있음.
    if n % 2 == 1:
        answer.append(A[-1])
    answer = ' '.join(answer)
    print(f'{tc} {answer}')
