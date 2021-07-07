def bus(idx, remain, cnt):
    global minC
    if minC <= cnt or remain < 0:
        return
    if idx == N-1:
        if minC > cnt:
            minC = cnt
        return
    else:
        bus(idx+1, arr[idx]-1, cnt+1)
        bus(idx+1, remain-1, cnt)


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    arr = arr[1:]
    remain = arr[0] - 1
    minC = N-1
    bus(1, remain, 0)
    print(f'#{tc} {minC}')