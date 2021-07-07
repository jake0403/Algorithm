def solution(N):
    # 1,3,5,7의 경우에 홀수로 더하는 값은 자기 자신밖에 없음
    if N == 1 or N == 3 or N == 5 or N == 7:
        return [N]
    # 2 일 경우 답이 없음
    elif N == 2:
        return [0]

    arr = [0] * (N + 1)
    a = 0
    u = 0
    for i in range(1,N,2):
        if a+i >= N:
            break
        arr[u] = i
        u+=1
        a+=i
    start = 0
    r = N-a
    if r%2 == 0:
        arr[u-1]+=r
    elif r >arr[u-1]:
        u+=1
        arr[u] = r
    else:
        start = 1
        arr[u-1]+=r+1
    arr = [x for x in arr if x]
    return arr



N = 11
print(solution(N))