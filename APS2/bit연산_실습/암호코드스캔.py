def verify(ans):
    even = ans[1] + ans[3] + ans[5]
    odd = (ans[0] + ans[2] + ans[4] + ans[6])*3
    v = ans[7]
    if (odd + even + v) % 10 == 0:
        return sum(ans)
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans = []
    check = []
    # 뒤에서부터 돌기 때문에 숫자 거꾸로
    num_code = {
        '112': 0,
        '122': 1,
        '221': 2,
        '114': 3,
        '231': 4,
        '132': 5,
        '411': 6,
        '213': 7,
        '312': 8,
        '211': 9,
    }

    for i in range(N):
        # 16 진수의 arr를 2진수 arr로 변환
        #arr[i] = ''.join([format(int(i,16),'04b') for i in arr[i]])
        temp = ''
        for j in range(M):
            temp += format(int(arr[i][j], 16), '04b')
        arr[i] = temp
    result = 0
    for i in range(N):
        # 뒤에서부터 1을 찾는데 생각해보니 앞에 자리가 없어도 숫자 분류가 가능
        # 3개로 10진수를 변환할 숫자 찾음
        d1 = d2 = d3 = 0
        # 한줄이 전부 0이면 pass
        if arr[i] == '0'*(M*4):
            continue
        for j in range(M*4-1, -1, -1):
            if not d2 and not d3 and arr[i][j] == '1':
                # 끝 자리 1의 연속된 1의 개수 파악
                d1+=1
            elif d1 and not d3 and arr[i][j] == '0':
                d2+=1
            elif d1 and d2 and arr[i][j] == '1':
                d3+=1
            elif d3 and arr[i][j] == '0':
                # 비율은 1을 포함하므로 가장 작은 수 찾아서 나눔
                ratio = min(d1,d2,d3)
                # 10진수 숫자로 변환 후 추가
                ans.append(num_code[str(d1//ratio)+ str(d2//ratio)+str(d3//ratio)])
                # 10진수로 변환한 숫자가 8개라면
                if len(ans) == 8:
                    # 검사한 숫자인지 판별
                    if ans not in check:
                        # 검사 안한 암호코드라면
                        # 검증
                        result+=verify(ans[::-1])
                        # 검사 했다고 체크
                        check.append(ans)
                    # 추가 했으니 초기화
                    ans = []
                # 10진수 변환할 변수 초기화
                d1 = d2 = d3 = 0
    print(f'#{tc} {result}')