T = int(input())
for tc in range(1,T+1):
    ans = ''
    words = [input() for x in range(5)]
    words_array = [[-1]*5 for y in range(15)]
    row = 0
    for w in words:
        col = 0
        for j in w:
            words_array[col][row] = j
            col+=1
        row+=1
    for r in words_array:
        for c in r:
            if c == -1:
                continue
            ans+=c
    print(f'#{tc} {ans}')
##############################################################################
