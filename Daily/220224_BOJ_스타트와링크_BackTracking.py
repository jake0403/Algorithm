import sys
input = lambda : sys.stdin.readline().strip()
from itertools import combinations
# def startlink(synergy):
#     global balance
#     if balance < synergy:
#         return
#     else:
#         balance = synergy
#         return
#
#     pass


balance = sys.maxsize

N = int(input())
m = list(range(N))
member = list(combinations(m, N//2))
teams = [list(map(int, input().split())) for _ in range(N)]
# for x in member:
#     team_s = team_l = 0
#     for i in range(N//2 -1):
#         pass
print(member)