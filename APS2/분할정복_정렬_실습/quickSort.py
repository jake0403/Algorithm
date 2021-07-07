def pivot(arr,pv,r):
    i = pv -1
    for j in range(pv,r):
        if arr[j] < arr[r]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def quickSort(arr, left, right):
    if left < right:
        p = pivot(arr, left, right)
        quickSort(arr, left, p-1)
        quickSort(arr, p+1, right)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quickSort(arr, 0, N-1)
    print(f'#{tc} {arr[N//2]}')