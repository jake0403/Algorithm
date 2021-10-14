def solution(lottos, win_nums):
    answer = []
    lottos.sort()
    win_nums.sort()
    remove_cnt = 0
    match = 0

    for i in range(6):
        if lottos[i] == 0:
            remove_cnt += 1
            continue
        for j in range(6):
            if lottos[i] == win_nums[j]:
                match += 1
                break
    if not remove_cnt:
        if not match:
            answer = [6, 6]
        else:
            answer = [7 - match, 7 - match]
    else:
        if not match:
            answer = [7 - remove_cnt, 6]
        else:
            answer = [7 - (match + remove_cnt), 7 - match]

    return answer

'''
https://programmers.co.kr/learn/courses/30/lessons/77484
'''