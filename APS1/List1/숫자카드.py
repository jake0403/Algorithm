T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    num = input()
    num_list = [int(x) for x in num]

    count_dict = {key: 0 for key, value in dict.fromkeys(num_list).items()}

    for i in num_list:
        count_dict[i]+=1
    max_v = 0
    max_c = 0
    for v, c in count_dict.items():
        if max_c < c:
            max_c = c
            max_v = v
        elif max_c == c :
            if max_v < v:
                max_v = v
    print(f'#{test_case} {max_v} {max_c}')
