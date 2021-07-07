# p ~ q, q+1 ~ r 병합
def merge(A, p, q, r):
    global cnt
    # 왼쪽 영역의 시작
    i = p
    # 오른쪽 영역의 시작
    j = q+1
    # i와 j를 교환할 정보를 저장할 리스트 생성
    tmp = [0] * (r-p+1)
    # 마지막 길이인 r - p + 1까지
    for k in range(r-p+1):
        if i <= q and j <= r:
            # i가 가리키는 애가 더 작으면 교환 안해도 됨
            # j가 가리키는 애가 더 작으면 교환 해야 됨
            if A[i] > A[j]:
                tmp[k] = A[j]
                j+=1
            else:
                tmp[k] = A[i]
                i+=1
        elif j <= r:
            tmp[k] = A[j]
            j+=1
        else:
            tmp[k] = A[i]
            i += 1
    for k in range(r-p+1):
        A[p+k] = tmp[k]


def mergeSort(A, p, r):
    if p < r:
        q = (p+r) // 2
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)


#A = [7, 4, 9, 3, 2, 11, 10, 8]
A = list(map(int, input().split()))
cnt = 0
mergeSort(A, 0, len(A)-1)
print(A)