from collections import defaultdict
def solution(record):
    answer = []
    records = [list(x.split()) for x in record]
    nickname = defaultdict(str)
    for r in records:
        if r[0] == 'Leave':
            continue
        nickname[r[1]] = r[2]
    for r in records:
        if r[0] == 'Enter':
            answer.append(f'{nickname[r[1]]}님이 들어왔습니다.')
        elif r[0] == 'Leave':
            answer.append(f'{nickname[r[1]]}님이 나갔습니다.')
    return answer