def rsp(card):
    n = len(card)
    if n <2:
        return card[0]
    if n % 2 == 0:
        left = card[:n//2]
        right = card[n//2:]
    else:
        left = card[:n//2+1]
        right = card[n//2+1:]
    L = rsp(left)
    R = rsp(right)
    if findWinner(L[0],R[0]):
        return L
    else:
        return R
def findWinner(L,R):
    if (L == 1 and R == 3) or (L == 1 and R ==1):
        return 1
    elif (L == 2 and R == 1) or (L ==2 and R ==2):
        return 1
    elif (L == 3 and R == 2) or (L ==3 and R ==3):
        return 1
    return 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    card = [(c, i+1) for i, c in enumerate(card)]
    print(f'#{tc} {rsp(card)[1]}')