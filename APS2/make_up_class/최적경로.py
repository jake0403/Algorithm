def shortest(idx, x, y, dist):
    global minD
    if dist >= minD:
        return
    if idx == N:
        dist += abs(x - home[0]) + abs(y - home[1])
        if dist < minD:
            minD = dist
        return

    for i in range(0, len(arr), 2):
        if not visited[i//2]:
            visited[i//2] = 1
            shortest(idx+1, arr[i], arr[i+1], dist + abs(x - arr[i]) + abs(y - arr[i+1]))
            visited[i//2] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    office = arr[0:2]
    home = arr[2:4]
    arr = arr[4:]
    minD = 2000
    visited = [0]*N
    shortest(0, office[0], office[1], 0)
    print(minD)