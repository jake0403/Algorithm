import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
totalP = list(permutations(list(range(1,10)), 3))

for _ in range(N):
    question, strike, ball = map(int, input().split())

    question = list(str(question))
    question = [int(x) for x in question]
    rmIndex = 0
    # 1부터 9까지 3개로 구성된 순열 전부 완전 탐색
    for i in range(len(totalP)):
        strike_cnt = ball_cnt = 0
        # 삭제한(가능성 없는) 숫자들 전체 수 만큼 index 처리 (Index Error 방지)
        i-=rmIndex
        for j in range(3):
            if question[j] in totalP[i]:
                if j == totalP[i].index(question[j]):
                    strike_cnt+=1
                else:
                    ball_cnt+=1
        # strike 숫자나 ball 숫자가 같지 않으면 가능성 없는 숫자이므로 삭제
        if strike != strike_cnt or ball != ball_cnt:
            del totalP[i]
            rmIndex+=1
print(len(totalP))



