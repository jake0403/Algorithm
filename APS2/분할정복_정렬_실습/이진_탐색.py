def binarySearch(arr, low, high, key, direct):
    global cnt
    # 찾는 값이 없으면
    if low > high:
        return
    else:
        mid = (low + high) // 2
        # 값이 맞을 때
        if key == arr[mid]:
            cnt+=1
            return
        # 찾는 값이 중간 값보다 작으면 왼쪽으로 이동
        elif key < arr[mid]:
            # 왼쪽으로 이동했을 때는 direct 값 = 0
            # 근데 왼쪽으로 한 번 더 이동할 경우 그냥 return
            if direct == 0:
                return
            # 그게 아니라면 direct 값 바꾸고 재귀
            else:
                direct = 0
                binarySearch(arr, low, mid-1, key, direct)
        # 찾는 값이 중간 값보다 큰 경우 오른쪽 이동
        else:
            # 오른쪽으로 이동했을 때는 direct 값 = 1
            # 이미 direct 값이 1(오른쪽)이라면 return
            if direct == 1:
                return
            # 그게 아니라면 direct 값 바꾸고 재귀
            else:
                direct = 1
                binarySearch(arr, mid+1, high, key, direct)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int,input().split())).sort()
    b = list(map(int, input().split()))
    cnt = 0
    # 왼쪽 오른쪽 간 횟수 판별
    direction = -1
    # b에 속한 어떤 수가 a에 들어있는지 => b의 원소 값이 key 값
    for key in b:
        binarySearch(a, 0, len(a)-1, key, direction )

    print(f'#{tc} {cnt}')