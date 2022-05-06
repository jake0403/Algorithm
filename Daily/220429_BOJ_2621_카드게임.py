import sys
input = lambda : sys.stdin.readline().strip()

card = [input() for _ in range(5)]
print(sorted(card, reverse=True))