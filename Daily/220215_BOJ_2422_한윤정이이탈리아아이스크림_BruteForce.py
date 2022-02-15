import sys
input = lambda : sys.stdin.readline().strip()

def dfs(flavor):
    global visited, answer
    if flavor == 3:
        for i in range(2):
            for j in range(1,3):
                if taste[j] in bad_taste[taste[i]]:
                    return
        answer+=1
        return
    for i in range(1, N+1):
        if not visited[i]:
            if taste and taste[-1] < i :
                    continue
            visited[i] = 1
            taste.append(i)
            dfs(flavor+1)
            visited[i] = 0
            taste.pop()


N, M = map(int, input().split())
bad_taste = [set() for _ in range(N+1)]
for i in range(M):
    h,t = map(int, input().split())
    bad_taste[h].add(t)
    bad_taste[t].add(h)
bad_taste = [list(x) for x in bad_taste]
visited = [0]*(N+1)
taste = []
answer = 0
dfs(0)
print(answer)