def attack(n):
    pass


T= int(input())
for tc in range(1,T+1):
    N = int(input())
    # 나라 정보
    country = [list(map(int, input().split())) for _ in range(N)]
    # 군대 정보
    army = [list(map(int, input().split())) for _ in range(N)]
    # 보충 정보
    make_up = [list(map(int, input().split())) for _ in range(N)]
