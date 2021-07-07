def makeChip():
    pass


T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    wayper = [list(map(int, input().split())) for _ in range(H)]

