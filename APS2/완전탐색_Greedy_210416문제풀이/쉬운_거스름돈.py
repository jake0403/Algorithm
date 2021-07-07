T = int(input())
for tc in range(1, T+1):
    money = int(input())
    change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    check = [0]*len(change)
    for i in range(len(change)):
        if money >= change[i]:
            check[i] = money//change[i]
            money %= change[i]
    check = [str(i) for i in check]
    check = ' '.join(check)
    print(f'#{tc}')
    print(check)