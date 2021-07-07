from collections import deque
def D(arr):
    arr = deque(arr)
    if len(arr) !=0:
        arr.popleft()
        return arr
    return 'error'


T = int(input())
for tc in range(T):
    func = input()
    N = int(input())
    arr = input()
    arr = arr[1:-1].split(',')
    for f in func:
        if f == 'R':
            arr = arr[::-1]
        else:
            arr = D(arr)
    for i in arr:
        print(i, end='')
    print()
