def recur(N):
    global cnt, result
    if cnt > 13:
        result = 'overflow'
        return
    if N == 0.0:
        return
    nxt = N * 2
    result+=str(int(nxt))
    cnt+=1
    N = nxt - int(nxt)
    recur(N)

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    result = ''
    cnt = 0
    recur(N)
    print(f'#{tc} {result}')