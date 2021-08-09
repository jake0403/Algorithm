from itertools import combinations
import sys
input = lambda : sys.stdin.readline().strip()

def lottery(a):
    a = a[1:]
    if not a:
        return
    a.sort()
    b = list(combinations(a,6))

    for i in range(len(b)):
        print(*b[i])


while True:
    a = list(map(int, input().split()))
    if not a[0]:
        break
    lottery(a)
    print()

