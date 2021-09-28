import sys
input = lambda: sys.stdin.readline().strip()
n = int(input())
game = [0]*(n+5)
# 돌 1개 3개일 때 창영 승
game[1] = game[3] = 0
# 돌 2개 4개일 때 상근 승
game[2] = game[4] = 1

for i in range(5, n+1):
    # 모두 처음 돌을 가져간 사람이 이기는 경우 (1,3,4 개 뺴도 이길 수 밖에 없는 경우)
    if game[i-1] and game[i-3] and game[i-4]:
        # 창영 승
        game[i] = 0
    # 하나라도 나중에 돌을 가져간 사람이 이기는 경우가 있으면
    else:
        # 상근 승
        game[i] = 1
if game[n]:
    print('SK')
else:
    print('CY')


