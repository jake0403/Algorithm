def drop():
    pass

T = int(input())
for tc in range(1, T+1):
    # N : 구슬 개수, W: 가로 길이,  H : 세로 길이
    N, W, H = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(H)]

    ans = []
