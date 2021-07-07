def findWinner(p1, p2):
    def checkTri(arr):
        own = [0] * 10
        # triplet 검사
        for i in arr:
            own[i]+=1
            if own[i] >= 3:
                return 1
        return 0
    def checkRun(arr):
        own = [0] * 10
        # run 검사
        for i in arr:
            own[i]+=1
        for i in range(len(arr)-3+1):
            if (own[i] and own[i+1] and own[i+2]) >= 1:
                return 1
        return 0
    p1W = checkTri(p1) or checkRun(p1)
    if p1W == 1:
        return 1
    p2W = checkTri(p2) or checkRun(p2)
    if p2W == 1:
        return 2
    if (p1W and p2W) == 0:
        return 0

T = int(input())
for tc in range(1, T+1):
    card = list(map(int,input().split()))
    p1 = []
    p2 = []
    for i in range(0,len(card),2):
        p1.append(card[i])
        p2.append(card[i+1])
        res = findWinner(p1,p2)
    print(f'#{tc} {res}')