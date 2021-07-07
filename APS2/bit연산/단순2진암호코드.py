def findstart(arr):
    for i in range(N):
        for j in range(M-1,-1,-1):
            if arr[i][j] == 1:
                return [i,j]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    code = [list(map(int, input())) for _ in range(N)]
    num_code = {
        '3211' : 0,
        '2221' : 1,
        '2122' : 2,
        '1411' : 3,
        '1132' : 4,
        '1231' : 5,
        '1114' : 6,
        '1312' : 7,
        '1213' : 8,
        '3112' : 9,
    }
    i, j = findstart(code)
    info = code[i][j-55: j+1]
    decode = []
    ans = ''
    result = []
    for i in range(0,len(info),7):
        decode.append(info[i:i+7])
    print(decode)
    for i in range(len(decode)):
        cnt = 1
        for j in range(1,len(decode[i])):
            if decode[i][j-1] == decode[i][j]:
                cnt+=1
                if j == len(decode[i]) - 1:
                    ans += str(cnt)
            else:
                ans+=str(cnt)
                cnt = 1
                if j == len(decode[i]) - 1:
                    ans += str(cnt)
    for i in range(0,len(ans), 4):
        result.append(ans[i:i+4])
    print(result)
    res = ''
    answer = 0
    verify = result[-1]
    for i,r in enumerate(result[:-1]):
        if i % 2  == 0:
            answer+=(num_code[r]*3)
        else:
            print(num_code[r])
            answer+=num_code[r]
    answer+=num_code[verify]
    if answer%10 != 0:
        print(f'#{tc} 0')
    else:
        ra = 0
        for r in result:
            ra+=num_code[r]
        print(f'#{tc} {ra}')