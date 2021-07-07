T = int(input())
for tc in range(1, T+1):
    short = input()
    sl = len(short)
    long = input()
    pin = short[-1]
    result = 0
    for i in range(sl-1,len(long)):
        if long[i] == pin:
            if long[i-(sl-1):i+1] == short:
                result =1
                break

    print(f'#{tc} {result}')
