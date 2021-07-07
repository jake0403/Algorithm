T = int(input())
for test in range(1, T+1):
    dump = int(input())
    boxes = list(map(int,input().split()))
    for i in range(dump):
        max_h = -1
        min_h = 101
        for b in boxes:
            if max_h < b:
                max_h = b
            if min_h > b:
                min_h = b
        boxes[boxes.index(max_h)]-=1
        boxes[boxes.index(min_h)]+=1
    new_max = -1
    new_min = 101
    for j in boxes:
        if new_max < j:
            new_max = j
        if new_min > j:
            new_min = j
    print(f'#{test} {new_max - new_min}')
