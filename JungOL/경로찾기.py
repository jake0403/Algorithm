from itertools import combinations
from collections import deque
def bfs(sv,ev):
    visited = [0]*(N+1)
    q = deque([sv])
    visited[sv] = 1
    ans = ''
    while q:
        n = q.popleft()
        if n == ev:
            return ans
        for i in range(1,N+1):
            if not visited[i] and node[n][i]:
                visited[i] = 1
                q.append(i)
                ans+=str(i)+' '


def dfs(sv, ev, cnt, st):
    global visit, node_arr, answer, min_cnt
    if cnt > min_cnt:
        return
    if sv == ev:
        if min_cnt > cnt:
            min_cnt = cnt
            answer = st
        return
    if node_arr[sv]:
        for i in node_arr[sv]:
            if not visit[i]:
                visit[i] = 1
                st+=str(i)+' '
                dfs(i,ev,cnt+1, st)


def H(a,b):
    cnt = 0
    for i in range(K):
        if code_arr[a][i] != code_arr[b][i]:
            cnt+=1
    if cnt == 1:
        return 1
    return 0

N, K = map(int, input().split())
code_arr = [0]*(N+1)
for i in range(1,N+1):
    code_arr[i] = input()
sn, en = map(int, input().split())
node = [[0]*(N+1) for _ in range(N+1)]
node_arr = [[] for _ in range(N+1)]
a = range(1,N+1)
combi = list(combinations(a,2))
for a,b in combi:
    if H(a,b):
        node[a][b] = 1
        node[b][a] = 1
        node_arr[a].append(b)
        node_arr[b].append(a)
answer = ''
min_cnt = 1000
visit = [0]*(N+1)
visit[sn] = 1
print(bfs(sn,en))
dfs(sn,en,0,str(sn)+' ')
print(answer)