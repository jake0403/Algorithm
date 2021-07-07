T = int(input())
for tc in range(1,T+1):
    N, R = map(int,input().split())
    queue = list(map(int, input().split()))

    for i in range(R):
        p = queue.pop(0)
        queue.append(p)
    print(f'#{tc} {queue[0]}')