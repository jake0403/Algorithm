# N = 버스 노선
# P = 버스 정류장 수
T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    station = [0] * 5001

    for i in range(n):
        a, b = map(int, input().split())
        for j in range(a, b + 1):
            station[j] += 1

    p = int(input())

    station_slice = [int(input()) for x in range(p)]

    print(f'#{tc}', end=' ')
    for k in range(p):
        if k == p - 1:
            print(station[station_slice[k]])
        else:
            print(station[station_slice[k]], end=' ')