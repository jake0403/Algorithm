def dfs(s, adj_d, e):
    global visited
    visited[s] = 1
    if s == e :
        return 1

    for i in adj_d[s]:
        if visited[i] == 0:
            result = dfs(i,adj_d,e)
            if result == 1:
                return result
    return -1

from collections import defaultdict
for i in range(10):
    tc, n = map(int, input().split())
    adj = list(map(int, input().split()))
    adj_l = [adj[x] for x in range(len(adj)) if x % 2 ==0 ]
    adj_r = [adj[x] for x in range(len(adj)) if x % 2 !=0 ]
    adj_dict = defaultdict(list)
    for i,j in zip(adj_l, adj_r):
        adj_dict[i]+=[j]
    visited = [0]*100
    e = 99
    print(f'#{tc} {dfs(0,adj_dict,e)}')
