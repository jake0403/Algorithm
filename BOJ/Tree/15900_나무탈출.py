import sys

input = lambda : sys.stdin.readline().strip()

N = int(input())
tree = [[] for _ in range(N+1)]

for i in range(N-1):
    pn, cn = map(int, input().split())
    tree[pn].append(cn)
    tree[cn].append(pn)

visited = [0] * (N+1)
stack = [[1,0]]
total = 0
# stack을 활용한 DFS
while stack:
    child, w = stack.pop()
    visited[child] = 1

    if child != 1 and len(tree[child]) == 1:
        total += w
        continue
    for cn in tree[child]:
        if not visited[cn]:
            stack.append([cn, w+1])

print(total)