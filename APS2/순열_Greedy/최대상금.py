def swap(i,n, cnt):
    global maxV, maxC
    # 모든 자리를 결정한 경우, 카운트가 남지 않은 경우는?
    if i == n or cnt ==0 :
        s =  0
        # 문자열을 숫자로 변환
        for k in range(n):
            s = s*10 + int(arr[k])
        # 큰 값 찾기
        if maxV <= s:
            maxV = s
            # maxC = maxV를 만들기까지 남은 교환 횟수
            if maxC > cnt:
                maxC = cnt
    else:
        # 왼쪽과도 교환이 가능
        # 원래는 for j in range(i,n)
        for j in range(n):

            arr[i], arr[j] = arr[j], arr[i]
            d = 0 if i==j else 1
            swap(i+1, n, cnt-d)
            arr[i], arr[j] = arr[j], arr[i]
T = int(input())
for tc  in range(1, T+1):
    arr, cnt = input().split()
    arr = list(arr)
    cnt = int(cnt)
    maxV = 0
    maxC = cnt
    swap(0, len(arr), cnt)
    # 교환 횟수가 홀수 번 남은 경우
    if maxC % 2 != 0:
        # 1의 자리 수
        n1 = maxV%10
        # 10의 자리 수
        n10 = maxV % 100 // 10
        maxV = maxV - (n10*10 + n1) + (n1*10 + n10)
    print(f'#{tc} {maxV}')