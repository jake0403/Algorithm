def binarySearch(total, key):
    start = 1
    end = total
    count = 1
    while start <= end:
        middle = (start + end )//2
        if middle == key:
            return count
        elif middle > key:
            count+=1
            end = middle
        else:
            count+=1
            start = middle
    return 10000


T = int(input())
for tc in range(1,T+1):
    end, A, B = map(int, input().split())
    #book = [i for i in range(end)]
    a_count = binarySearch(end, A)
    b_count = binarySearch(end, B)
    if a_count < b_count: winner =  "A"
    elif a_count > b_count: winner = "B"
    else: winner = 0
    print(f'#{tc} {winner}')