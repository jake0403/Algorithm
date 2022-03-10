def solution(new_id):
    ss = ['-', '_', '.']
    # 1, 2 단계
    answer = ''.join(x for x in new_id if x.isalnum() or x in ss).lower()
    # 3 단계
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4 단계
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    # 5 단계
    answer = 'a' if answer == '' else answer
    # 6 단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7 단계
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]

    return answer
new_id = '...!@BaT#*..y.abcdefghijklm'
print(solution(new_id))