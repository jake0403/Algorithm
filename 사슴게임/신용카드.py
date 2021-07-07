def solution(card_num):
    n = len(card_num)
    answer = ''
    card_num = [int(x) for x in card_num]
    if n % 2 == 0:
        for i in range(n):
            if i % 2 == 0:
                card_num[i]*=2
    else:
        for i in range(n):
            if i % 2 != 0:
                card_num[i]*=2
    card_num= ''.join(map(str,card_num))
    total = sum([int(x) for x in card_num])
    if total % 10 == 0:
        answer = 'VALID'
    else:
        answer = 'INVALID'
    return answer



card_num = '11111101'
print(solution(card_num))