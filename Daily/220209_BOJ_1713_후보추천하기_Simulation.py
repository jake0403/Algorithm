import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().strip()

N = int(input())    # 사진틀 수
total = int(input())    # 추천 횟 수
candidate = list(map(int, input().split()))  # 후보자들
vote_cnt = defaultdict(int)

for c in candidate:
    if len(vote_cnt) == N and c not in vote_cnt.keys():
        student = list(vote_cnt.keys())
        cnt = list(vote_cnt.values())
        tmp = cnt.index(min(cnt))
        idx = student[tmp]
        del vote_cnt[idx]

    vote_cnt[c] += 1
ans = sorted(vote_cnt.keys())
print(*ans)
