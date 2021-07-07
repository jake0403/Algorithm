T = int(input())
for tc in range(1, T+1):
    N , Q = map(int,input().split())
    change = [list(map(int, input().split())) for x in range(Q)]
    answer = [0]*N
    for i in range(len(change)):
        start = change[i][0]-1
        end = change[i][1]
        answer[start: end] = [i+1 for _ in range(start,end)]
    answer = ' '.join([str(i) for i in answer])
    print(f'#{tc} {answer}')