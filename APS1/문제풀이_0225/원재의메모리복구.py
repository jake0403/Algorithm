T = int(input())
for tc in range(1, T+1):
    memory = list(input())
    init = ['0']*len(memory)
    count = 0
    # 두 개의 값이 같아질 동안 반복
    while memory != init:
        for i in range(len(memory)):
            # 값이 같으면 pass
            if memory[i] == init[i] :
                continue
            else:
                # 값이 같지 않으면 init의 값 끝까지 같은 값으로 변경
                init[i:] = [memory[i] for x in init[i:]]
                # count 추가
                count+=1
    print(f'#{tc} {count}')
