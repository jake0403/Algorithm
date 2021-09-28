import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())

# 돌이 한 개 남거나 3개 남았을 때만 창영이가 승리
# 반복은 7개 단위로 반복 됨 => N을 7로 나눈 나머지가 1이나 3이면 창영 승리
if n % 7 == 1 or n % 7 == 3:
    print('CY')
else:
    print('SK')