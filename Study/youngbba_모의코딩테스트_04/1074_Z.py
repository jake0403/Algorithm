import sys
input = lambda : sys.stdin.readline().strip()

N, r, c = map(int, input().split())
answer = 0
while N > 1:
    # 4등분으로 쪼개기
    divide = 2 ** (N-1)
    if r < divide:          # (1, 2 사분면) 4등분 첫 번째, 두 번째
        if c < divide:      # 2사분면 ( 4등분 첫 번째)
            pass
        else:               # 1사분면 ( 4등분 두 번째)
            c-=divide
            answer += 4 ** (N-1) * 1
    else:                   # (3, 4 사분면) 4등분 세 번째, 네 번째
        r -= divide
        if c < divide:      # 3사분면
            answer += 4 ** (N-1) * 2
        else:               # 4사분면
            answer += 4 ** (N-1) * 3
            c -= divide
    N -= 1      # 계속 4등분으로 쪼개기

if r:
    if c: answer+=3
    else: answer+=2
else:
    if c : answer+=1

print(answer)
