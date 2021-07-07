T = int(input())
for tc in range(1,T+1):
    stick_array = input()
    stick = cnt = 0
    for i in range(len(stick_array)):
        #막대기인지 레이저인지 판별할 값
        sol = stick_array[i]
        #열린 괄호면 다음 값이 뭔지 몰라 막대기 or 레이져 일 수 있으므로 일단 더함
        if sol == '(':
            stick+=1
            cnt+=1
            # 첫 번째 값일 때는 pass
            if i ==0:
                continue
        # 닫힌 괄호면
        else:
            #그 전에 값이 열린괄호면 레이져이므로 더해준 값 빼주고 cnt stick 값 더해줌(잘린 막대기)
            if stick_array[i-1] == '(':
                stick-=1
                cnt-=1
                cnt+=stick
            # 그게 아니라면 막대기
            else:
                stick-=1
    print(f'#{tc} {cnt}')

