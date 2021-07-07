T = int(input())
for tc in range(1, T+1):
    word = input()
    stack = []
    table = {
        ')' : '(',
        '}' : '{',
    }
    answer = 1
    for w in word:
        if w == '(':
            stack.append(w)
        elif w == '{':
            stack.append(w)
        if w in table:
            if not stack or stack.pop() != table[w]:
                answer = 0

    if stack: answer = 0
    print(f'#{tc} {answer}')