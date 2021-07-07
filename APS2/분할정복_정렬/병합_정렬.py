def merge_sort(arr):
    n = len(arr)
    if n == 1: return arr
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    # 재귀로 왼쪽 오른쪽 중간으로 나눠서 정렬할 상태로 만들기
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    global cnt
    # 왼쪽 오른쪽의 총 길이
    ll, rl = len(left), len(right)
    # 작은 값 고를 idx 변수 생성
    i, j = 0, 0
    # result 값 변경할 변수 생성
    r= 0
    # 정렬할 결과 값 저장할 리스트 생성
    result = [0] * (ll+rl)
    # 문제 조건에 따른 왼쪽 끝 값과 오른쪽 끝 값 비교
    if left[-1] > right[-1]:
        cnt+=1
    # 왼쪽 인덱스 값과 오른쪽 인덱스 값이 그 길이를 넘지 않을 때 까지
    while i < ll and j < rl:
        # 왼쪽 값이 더 작으면
        if left[i] <= right[j]:
            # 정렬된 값 저장 후
            result[r] = left[i]
            # 왼쪽 idx 값 오른쪽으로 이동
            i+=1
            r+=1
        # 오른쪽 값이 더 작으면
        else:
            result[r] = right[j]
            j+=1
            r+=1
    # 왼쪽 값이 남아 있을 경우
    if i < ll:
        while i < ll:
            result[r] = left[i]
            i+=1
            r+=1
    # 오른쪽 값이 남아 있을 경우
    if j <rl:
        while j < rl:
            result[r] = right[j]
            j+=1
            r+=1
    return result




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    print(f'#{tc} {merge_sort(arr)[N//2]} {cnt}')
