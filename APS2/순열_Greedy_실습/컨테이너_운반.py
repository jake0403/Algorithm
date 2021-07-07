T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cargo = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)
    load = 0
    for i in range(M):
        res = 0
        for c in cargo:
            if c <= truck[i]:
                res = c
                break
        if res != 0:
            cargo.remove(res)
        load += res
    print(load)