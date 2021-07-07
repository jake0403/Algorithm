T = int(input())
for tc in range(1, T+1):
    str_list = list(input())
    answer = []
    answer.append(str_list.pop(0))
    for i in str_list:
        if answer and i == answer[-1]:
            answer.pop()
        else:
            answer.append(i)
    print(f'#{tc} {len(answer)}')