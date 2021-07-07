n , q = map(int,input().split())
card = [0] * n
for i in range(1,q+1):
    case = []
    rang = list(map(int, input().split()))
    case.append(rang)
    for j in case:
        card[j[0]-1:j[1]] = [i]*(j[1]-j[0]+1)
card = [str(x) for x in card]
card = ' '.join(card)
print(card)