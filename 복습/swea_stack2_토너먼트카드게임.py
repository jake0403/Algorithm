# 1 = 가위, 2 = 바위, 3 = 보
def tournement(player):
    pass


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    player = list(map(int,input().split()))
    player = [(i,v) for i,v in enumerate(player)]
