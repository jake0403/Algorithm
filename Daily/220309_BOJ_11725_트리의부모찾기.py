from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

def bfs(n):
    q = deque([])
    q.append(n)
    while q:
        n = q.popleft()
        visitedB[n] = 1
        for c in node[n]:
            if visitedB[c] == 0:
                q.append(c)
                answerB[c] = n
N = int(input())
node = [[] for _ in range(N+1)]
visitedB = [0]*(N+1)
answerB = [0]*(N+1)

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    node[n1].append(n2)
    node[n2].append(n1)

bfs(1)
answerB = answerB[2:]
for answer in answerB:
    print(answer)
