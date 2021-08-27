import sys
input = lambda : sys.stdin.readline().strip()

N = int(input())
balloon = list(range(1,N+1))
card = list(map(int, input().split()))

idx = 0
move = card.pop(idx)
result = [balloon.pop(idx)]
while card:
    if move < 0:
        idx = (move + idx) % len(card)
    else:
        idx = (move + idx -1) % len(card)
    move = card.pop(idx)
    result.append(balloon.pop(idx))
for i in result:
    print(i, end=" ")