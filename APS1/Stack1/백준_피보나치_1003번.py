T = int(input())
for i in range(T):
    n = int(input())
    arr = [0] * 41
    arr[1] = arr[2] = 1
    for i in range(3,41):
        arr[i] = arr[i-1] + arr[i-2]
    print(f'{arr[n-1]} {arr[n]}') if n > 0 else print('1 0')