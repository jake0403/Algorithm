import sys
input = lambda : sys.stdin.readline().strip()

def energy(b):
    global max_e
    if len(biz) == 2:
        max_e = max(max_e, b)
        return

    for i in range(1, len(biz)-1):
        n = biz[i-1] * biz[i+1]
        tmp = biz[i]
        del biz[i]
        energy(b + n)
        biz.insert(i, tmp)


N = int(input())
biz = list(map(int, input().split()))
max_e = 0
energy(0)
print(max_e)