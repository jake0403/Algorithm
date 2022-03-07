def solution(s):
    x = cnt = 0
    c = s.count('0')
    a = len(s) - c
    while s != "1":
        cnt += 1
        c = s.count('0')
        x += c
        a = len(s) - c
        s = format(a, 'b')
    answer = [cnt, x]

    return answer

s = "111010111101"