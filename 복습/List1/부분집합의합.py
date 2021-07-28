T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = range(1,13)
    answer = 0
    for i in range(12 - n+1):
        if sum(arr[i:n]) == k:
            answer+=1
    print(f'#{tc} {answer}')


# Wrong Answer

## 비트 연산 다시 공부