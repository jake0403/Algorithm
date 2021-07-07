T = int(input())
for tc in range(1, T+1):
    n = int(input())
    product = list(map(int, input().split()))
    product = product[::-1]
    profit = 0
    max_p = product[0]
    for i in range(1, n):
        if max_p > product[i]:
            profit+= max_p-product[i]
        else:
            max_p = product[i]

    print(f'#{tc} {profit}')