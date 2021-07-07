T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work = list(map(int,input().split()))
    total = 0
    for w in work:
        total+=w
    min_num = total
    index = 0
    answer = []
    sumn = 0
    for i in range(N-1):
        sumn += work[i]
        x = total-sumn*2
        if x < 0 : x = -x
        answer.append([x, i])
    print(answer)
    for i in answer:
        if min_num > i[0]:
            min_num = i[0]
            index = i[1]


    print(f'#{tc} {index+1} {min_num}')