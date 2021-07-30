from collections import defaultdict
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
memo = defaultdict(str)
for i in range(N):
    memo[input().rstrip()] = 1
post =[]
for i in range(M):
    post+=input().rstrip().split(",")
    post.append('/')

for p in post:
    if p.rstrip() == "/":
        print(N)
    if memo[p.rstrip()]:
        memo[p.rstrip()] = 0
        N-=1