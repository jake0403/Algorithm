from collections import deque
def hideNSeek():
    q = deque()
    q.append(N)
    while q:
        now = q.popleft()
        if now == K:
            return dist[now]
        for dn in ([now+1, now-1, now*2]):
            if 0<= dn <= max_num and dist[dn] == 0:
                dist[dn] = dist[now]+1
                q.append(dn)
    return 0

N, K = map(int, input().split())
max_num = 10 ** 5
dist = [0] * (max_num + 1)
answer = hideNSeek()
print(answer)