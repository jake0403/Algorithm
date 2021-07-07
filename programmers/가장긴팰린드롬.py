def solution(s):
    answer = ''
    if len(s) < 2 or s == s[::-1]:
        return len(s)

    def sliding_window(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left-=1
            right+=1
        return s[left+1:right]

    for i in range(len(s)-1):
        answer = max(answer, sliding_window(i,i+1), sliding_window(i, i+2) ,key=len)
    return len(answer)

s = 'bbbcccadfeeefsas'
print(solution(s))