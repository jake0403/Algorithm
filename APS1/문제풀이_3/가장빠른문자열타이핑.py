T = int(input())
for tc in range(1,T+1):
    A , B = map(str, input().split())
    answer = A.replace(B,'1')
    print(f'#{tc} {len(answer)}')